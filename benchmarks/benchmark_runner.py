import json
import pandas as pd

from providers.gemini_provider import GeminiProvider
from providers.grok_provider import GroqProvider


providers = {
    
    "groq": GroqProvider(),
}


def run_factual():

    with open("../datasets/factual.json") as f:
        data = json.load(f)

    rows = []

    for model_name, provider in providers.items():

        correct = 0

        for item in data:

            response = provider.generate(
                item["question"],
                []
            )

            if item["expected"].lower() in response.lower():
                correct += 1

        rows.append({
            "model": model_name,
            "accuracy": round(
                correct / len(data) * 100,
                2
            )
        })

    return pd.DataFrame(rows)