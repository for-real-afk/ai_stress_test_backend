import json
from datetime import datetime
from pathlib import Path


class ObservabilityService:

    LOG_FILE = (
        Path(__file__).resolve().parent.parent
        / "logs"
        / "interactions.jsonl"
    )

    @staticmethod
    def log(
        model,
        prompt,
        response,
        latency,
        prompt_tokens,
        response_tokens,
        cost
    ):

        record = {

            "timestamp":
                str(datetime.utcnow()),

            "model":
                model,

            "latency":
                latency,

            "prompt_tokens":
                prompt_tokens,

            "response_tokens":
                response_tokens,

            "total_tokens":
                prompt_tokens +
                response_tokens,

            "cost":
                cost,

            "prompt":
                prompt,

            "response":
                response
        }

        with open(
            ObservabilityService.LOG_FILE,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                json.dumps(record)
            )

            f.write("\n")