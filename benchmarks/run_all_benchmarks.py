from benchmark_runner import run_factual
from memory_benchmark import run
from safety_benchmark import run as run_safety

print("\n===== FACTUAL =====")
print(run_factual())

print("\n===== MEMORY =====")
print(run())

print("\n===== SAFETY =====")
print(run_safety())