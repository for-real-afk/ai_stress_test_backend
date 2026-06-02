import json
import time
from pathlib import Path
from typing import Dict, Any, List


class ObservabilityService:
    """
    Logs:
    - Model used
    - Input tokens
    - Output tokens
    - Total tokens
    - Latency
    - Estimated cost
    - Timestamp

    Data stored as JSONL for easy analytics.
    """

    LOG_DIR = Path("logs")
    LOG_FILE = LOG_DIR / "interactions.jsonl"

    @classmethod
    def initialize(cls):
        """
        Create logs directory/file if missing.
        """
        cls.LOG_DIR.mkdir(parents=True, exist_ok=True)

        if not cls.LOG_FILE.exists():
            cls.LOG_FILE.touch()

    @classmethod
    def log(
        cls,
        model: str,
        prompt: str,
        response: str,
        latency: float,
        input_tokens: int,
        output_tokens: int,
        cost: float = 0.0,
    ):

        try:
            cls.initialize()

            entry = {
                "timestamp": time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "model": model,
                "prompt": prompt[:500],
                "response": response[:500],
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": input_tokens + output_tokens,
                "latency": round(latency, 2),
                "cost": round(cost, 6),
            }

            with open(
                cls.LOG_FILE,
                "a",
                encoding="utf-8"
            ) as f:
                f.write(
                    json.dumps(entry, ensure_ascii=False)
                    + "\n"
                )

        except Exception as e:
            print(
                f"[OBSERVABILITY ERROR] {e}"
            )

    @classmethod
    def load_metrics(cls) -> List[Dict[str, Any]]:

        try:

            cls.initialize()

            records = []

            with open(
                cls.LOG_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                for line in f:
                    line = line.strip()

                    if not line:
                        continue

                    try:
                        records.append(
                            json.loads(line)
                        )
                    except Exception:
                        pass

            return records

        except Exception as e:
            print(
                f"[OBSERVABILITY LOAD ERROR] {e}"
            )
            return []

    @classmethod
    def summary(cls):

        data = cls.load_metrics()

        if not data:
            return {
                "requests": 0,
                "avg_latency": 0,
                "total_tokens": 0,
                "total_cost": 0,
            }

        total_requests = len(data)

        total_tokens = sum(
            x.get("total_tokens", 0)
            for x in data
        )

        total_cost = sum(
            x.get("cost", 0)
            for x in data
        )

        avg_latency = (
            sum(
                x.get("latency", 0)
                for x in data
            )
            / total_requests
        )

        return {
            "requests": total_requests,
            "avg_latency": round(
                avg_latency,
                2
            ),
            "total_tokens": total_tokens,
            "total_cost": round(
                total_cost,
                4
            ),
        }