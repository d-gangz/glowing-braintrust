# Braintrust Testing Project

A collection of scripts for testing [Braintrust](https://www.braintrust.dev/) evaluation functionalities and prompt chaining.

## Project Overview

This project demonstrates various ways to use Braintrust for evaluating LLM prompt chains and structured outputs. It includes examples of:

- Prompt chaining with multiple models
- Structured output evaluation
- Integration with Braintrust's datasets and evaluation metrics
- Custom evaluation scripts

## Scripts

### `eval_prompts.py`

Tests a two-prompt chain using manually defined data. This script:
- Chains "storyoutline-geminiFlash001" and "story-4omini" prompts
- Uses an in-memory dataset with fiction genres
- Shows basic prompt chaining patterns

### `eval_so.py`

Demonstrates structured output evaluation with:
- Two-prompt chain with structured output
- Integration with datasets stored in Braintrust
- Metadata tracking for experiments

### `eval_tester.py`

A minimal example showing:
- Basic Braintrust evaluation setup
- Integration with autoevals for factuality testing
- Simple lambda function for evaluation

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the environment:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install braintrust-dev python-dotenv autoevals`
5. Create a `.env` file with your Braintrust API key
6. Run any script: `python eval_prompts.py`

## Environment Variables

Required in `.env` file:
```
BRAINTRUST_API_KEY=your_api_key_here
```

## Project Structure

- `.venv/`: Virtual environment
- `eval_prompts.py`: Script for testing prompt chains
- `eval_so.py`: Script for testing structured output evaluation
- `eval_tester.py`: Minimal evaluation example
- `.env`: Environment variables (not tracked in git)

## Resources

- [Braintrust Documentation](https://www.braintrust.dev/docs)
- [Braintrust Python SDK](https://github.com/braintrust-ai/braintrust-sdk)
- [Auto-Evals Library](https://github.com/braintrust-ai/autoevals) 