from pathlib import Path
import json
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent

LOG_FILE = (
    ROOT_DIR /
    "backend" /
    "logs" /
    "interactions.jsonl"
)

def load_metrics():

    rows = []

    if not LOG_FILE.exists():
        return pd.DataFrame()

    with open(
        LOG_FILE,
        encoding="utf-8"
    ) as f:

        for line in f:
            rows.append(
                json.loads(line)
            )

    return pd.DataFrame(rows)