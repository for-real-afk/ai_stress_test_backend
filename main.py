from fastapi import FastAPI
from pydantic import BaseModel
from services.token_counter import TokenCounter

from services.observability_service import (
    ObservabilityService
)

from services.cost_estimator import (
    CostEstimator
)

from services.safety_guardrails import (
    SafetyGuardrails
)

from providers.gemini_provider import (
    GeminiProvider
)

from providers.grok_provider import GroqProvider


from services.memory_service import (
    MemoryService
)

from services.evaluation_service import (
    EvaluationService
)


app = FastAPI(
    title="AI Stress Test Lab"
)


memory = MemoryService()

providers = {
    "gemini": GeminiProvider(),
    "groq": GroqProvider()
}


class ChatRequest(
    BaseModel
):

    model: str
    message: str


@app.get("/")
def home():

    return {
        "status": "running"
    }

@app.get("/")
def health():

    return {
        "status": "ok",
        "project": "AI Stress Test Lab"
    }
@app.post("/chat")
def chat(request: ChatRequest):

    allowed = SafetyGuardrails.check(
        request.message
    )

    if not allowed:

        return {
            "response":
            "Request blocked by safety layer.",
            "latency": 0,
            "cost": 0
        }

    provider = providers[
        request.model
    ]

    context = memory.get_context()

    result = (
        EvaluationService.evaluate(
            provider,
            request.message,
            context
        )
    )

    prompt_tokens = (
        TokenCounter.count(
            request.message
        )
    )

    response_tokens = (
        TokenCounter.count(
            result["response"]
        )
    )

    cost = (
        CostEstimator.estimate(
            request.model,
            prompt_tokens +
            response_tokens
        )
    )

    ObservabilityService.log(
    model=request.model,
    prompt=request.message,
    response=response_text,
    latency=latency,
    input_tokens=input_tokens,
    output_tokens=output_tokens,
    cost=cost
    )

    memory.add_user(
        request.message
    )

    memory.add_assistant(
        result["response"]
    )

    return {
        "response":
        result["response"],

        "latency":
        result["latency"],

        "cost":
        cost,

        "prompt_tokens":
        prompt_tokens,

        "response_tokens":
        response_tokens
    }
@app.get("/analytics")
def analytics():

    return {
        "summary":
            ObservabilityService.summary(),
        "logs":
            ObservabilityService.load_metrics()
    }
@app.post("/reset")
def reset():

    memory.clear()

    return {
        "message": "memory reset"
    }