from benchmark_runner import (
    run_factual
)

import plotly.express as px

results = run_factual()

fig = px.bar(
    results,
    x="model",
    y="accuracy",
    title="Factual Accuracy"
)

fig.write_image(
    "../reports/factual_accuracy.png"
)

print(
    "report generated"
)