class CostEstimator:

    MODEL_COSTS = {

        "gemini": 0.00015,

        "grok": 0.00020,

        "qwen": 0.00001
    }

    @classmethod
    def estimate(
        cls,
        model,
        tokens
    ):

        cost_per_1k = (
            cls.MODEL_COSTS.get(
                model,
                0
            )
        )

        return round(
            (tokens / 1000)
            * cost_per_1k,
            6
        )