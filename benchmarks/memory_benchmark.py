import json

from providers.gemini_provider import GeminiProvider
from providers.grok_provider import GroqProvider


providers = {
    
    "groq": GroqProvider()
}


def run():

    with open("../datasets/memory.json", "r") as f:
        tests = json.load(f)

    results = []

    for model_name, provider in providers.items():

        score = 0

        for test in tests:

            context = [
                {
                    "role": "user",
                    "content": test["setup"]
                }
            ]

            response = provider.generate(
                test["query"],
                context
            )

            if test["expected"].lower() in response.lower():
                score += 1

        results.append(
            {
                "model": model_name,
                "memory_score": round(
                    score / len(tests) * 100,
                    2
                )
            }
        )

    return results


if __name__ == "__main__":
    print(run())