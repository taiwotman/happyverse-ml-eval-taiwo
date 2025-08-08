"""
# Happyverse ML Evaluation System

## Overview
This repository implements a prototype evaluation pipeline for analyzing interview transcripts against a technical job description using LLM-based agents. It outputs a candidate score and a visual slide summary.

## Tech Stack
- LangChain (for agent orchestration)
- OpenAI GPT-4 (as LLM backend)
- Pandas / Matplotlib (for data/slide visuals)
- Streamlit (optional UI)

## Key Modules
- **Transcript Evaluator**: Uses prompt templates and structured parsing to assess candidate answers.
- **Factual Verifier**: Identifies fabricated terms or unsupported claims.
- **Visualization Generator**: Creates a one-slide summary with candidate recommendation.

## Evaluation Dimensions
1. **Plausibility**: Do claims align with known technology?
2. **Technical Proficiency**: Are the answers accurate and well-scoped?
3. **Communication**: Is storytelling fluid and clear?

## Pipeline Design
```text
[Job Description + Questions + Transcript] --> LangChain Agent --> Score Generator --> PDF Visual Slide
```

## Edge Case Handling
- Detects hallucinations using keyword validation + few-shot prompt anchors
- Flags over-jargonization or buzzword stuffing
- Scales with prompt injection + modular transcript ingestion

## Extendability
- Easily swap job roles and question sets
- Add memory for multi-turn evaluations
- Integrate Retrieval (RAG) for real-time verification

## How to Run
```bash
pip install -r requirements.txt
python src/eval_pipeline.py
```

OR 
## Follow these steps to run in Jupyter Notebook

- Assumption: For sys path compatibility use: `MAC Os`.   

- Start Juypter notebook on Terminal: `jupyter notebook` and open in browser

- Run notebook: `notebooks/prototype_eval.ipynb`

---
## For addition support
Contact: Taiwo Adetiloye  
Email: taiwo.adetiloye@gmail.com
"""
