
# CodeReviewTool

This is a Python tool to perform code reviews on uncommitted changes using OpenAI API.

## Installation

First, make sure Poetry is installed on your system. If not, install it following the instructions at https://python-poetry.org/docs/.

To set up the project, run:

```bash
poetry install
```

## Usage

Before running the script, ensure you have set the `OPENAI_API_KEY` environment variable with your OpenAI API key.

To run the code review tool, navigate to your git repository with uncommitted changes and run:

```bash
poetry run python scripts/code_review.py
```
