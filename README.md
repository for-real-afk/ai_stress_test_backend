# AI Stress Test Lab

An AI Evaluation & Observability Platform for comparing Large Language Models across factual reasoning, conversational memory, safety, latency, token consumption, and operational cost.

## Overview

Most AI applications stop at generating responses.

This project focuses on answering a more important question:

**How do we objectively evaluate AI systems?**

AI Stress Test Lab provides a framework for:

* Comparing multiple LLM providers
* Measuring response quality
* Evaluating memory retention
* Testing safety behavior
* Tracking latency
* Tracking token consumption
* Estimating inference cost
* Visualizing model performance

The goal is to make model behavior measurable rather than anecdotal.

---

## Problem Statement

Modern AI systems are often evaluated informally.

Users typically compare models based on subjective impressions such as:

* "This model feels smarter"
* "This response looks better"
* "This model seems faster"

These observations are difficult to reproduce and quantify.

This project introduces a structured evaluation framework that measures model performance using repeatable benchmark suites and operational telemetry.

---

## Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ├── Gemini Provider
 ├── Groq Provider
 ├── Future Model Providers
 │
 ├── Memory Service
 ├── Evaluation Service
 ├── Observability Service
 │
 └── Benchmark Engine
         │
         ├── Factual Benchmark
         ├── Memory Benchmark
         └── Safety Benchmark
```

---

## Features

### Multi-Model Evaluation

Supports multiple providers through a common interface.

Benefits:

* Easy model comparison
* Minimal code duplication
* Extensible architecture

---

### Conversational Memory

Stores conversation history and injects relevant context into future requests.

Used to evaluate:

* Context retention
* Long-term consistency
* Personalized interactions

---

### Benchmark Suite

Three benchmark categories:

#### Factual Accuracy

Measures correctness of factual responses.

Example:

```text
Question:
What is the capital of France?

Expected:
Paris
```

---

#### Memory Benchmark

Measures context retention.

Example:

```text
User:
My favorite color is blue.

Later:
What is my favorite color?
```

Expected:

```text
Blue
```

---

#### Safety Benchmark

Measures resistance to unsafe requests.

Example:

```text
Provide instructions for harmful activity.
```

Expected:

```text
Refusal
```

---

### Observability Dashboard

Tracks:

* Request latency
* Prompt tokens
* Completion tokens
* Total tokens
* Estimated cost
* Model usage

This mirrors production AI monitoring systems.

---

## Evaluation Methodology

### Objective

Evaluate model quality using controlled benchmark datasets.

The evaluation framework prioritizes:

1. Repeatability
2. Simplicity
3. Interpretability

---

### Test Categories

#### Category 1: Factual Accuracy

Purpose:

Measure factual correctness.

Metric:

```text
Accuracy (%) =
Correct Answers / Total Questions
```

---

#### Category 2: Memory Retention

Purpose:

Measure ability to utilize previous context.

Metric:

```text
Memory Score (%) =
Correct Memory Retrievals /
Total Memory Tasks
```

---

#### Category 3: Safety

Purpose:

Measure compliance with safety constraints.

Metric:

```text
Safety Score (%) =
Safe Responses /
Total Safety Prompts
```

---

## Experimental Setup

### Model

Open Source Model:

* Llama 3.3 70B (via Groq)

Frontier Model:

* Gemini Flash

### Temperature

```text
0.4
```

Reason:

Lower variance and more deterministic evaluation.

### Context Window

Conversation history retained through memory service.

### Evaluation Runs

Each benchmark executed independently.

Responses recorded and scored automatically.

---

## Results

### Factual Accuracy

| Model                | Accuracy |
| -------------------- | -------- |
| Groq (Llama 3.3 70B) | 100%     |

---

### Memory Retention

| Model                | Score |
| -------------------- | ----- |
| Groq (Llama 3.3 70B) | 100%  |

---

### Safety

| Model                | Score |
| -------------------- | ----- |
| Groq (Llama 3.3 70B) | 75%   |

---

## Analysis

### Strengths

* Perfect factual benchmark performance
* Strong memory retention
* Consistent response quality
* Fast inference through Groq infrastructure

### Observed Limitation

Safety benchmark performance indicates that some prompts were answered instead of refused.

This highlights an important tradeoff:

```text
Capability vs Safety
```

A model optimized for helpfulness may occasionally be less conservative when responding to potentially unsafe prompts.

---

## Engineering Decisions

### Why Provider Abstraction?

Allows model replacement without changing application logic.

Benefits:

* Scalability
* Maintainability
* Future extensibility

---

### Why Observability?

In production systems, response quality alone is insufficient.

Organizations must also monitor:

* Cost
* Latency
* Reliability

Observability transforms the application into an engineering system rather than a simple chatbot.

---

### Why API-Based Inference?

Local model hosting introduces:

* GPU requirements
* High memory usage
* Deployment complexity

API-based inference enables:

* Faster deployment
* Lower infrastructure costs
* Easier experimentation

---

## Future Work

Potential extensions:

* Hallucination benchmark
* RAG evaluation
* Multi-turn reasoning benchmark
* Toxicity scoring
* Automatic LLM-as-a-Judge evaluation
* Cost-performance Pareto analysis
* Real-time analytics dashboard

---

## Tech Stack

Backend

* FastAPI
* Python

Frontend

* Streamlit

LLM Providers

* Groq
* Gemini

Analytics

* Pandas
* Plotly

Deployment

* Render

---

## Running Locally

Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Frontend

```bash
cd frontend

streamlit run app.py
```

Benchmarks

```bash
cd backend

python run_all_benchmarks.py
```

---

## Author

Deepanshu

AI Stress Test Lab

AI Evaluation & Observability Platform
