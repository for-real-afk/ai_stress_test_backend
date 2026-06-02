import time


class EvaluationService:

    @staticmethod
    def evaluate(
        provider,
        prompt,
        context
    ):

        start = time.time()

        response = provider.generate(
            prompt,
            context
        )

        latency = round(
            time.time() - start,
            2
        )

        return {
            "response": response,
            "latency": latency
        }