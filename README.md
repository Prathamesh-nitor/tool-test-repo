# LangGraph Calculator Application

A LangGraph-based calculator application that understands natural language arithmetic expressions and returns computed results.

## Features

- Natural language arithmetic expression parsing
- Support for basic operations: addition, subtraction, multiplication, division, exponentiation
- Support for parentheses and complex expressions
- Error handling for invalid expressions
- LangGraph state management
- Comprehensive logging

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and add your OpenAI API key:
```bash
cp .env.example .env
```

## Usage

Run the calculator application:
```bash
python main.py
```

Or use it programmatically:
```python
from workflows.calculator_graph import create_calculator_graph

app = create_calculator_graph()
result = app.invoke({
    "expression": "What is 25 + 17 multiplied by 3?"
})
print(result["result"])
```

## Project Structure

- `main.py` - Entry point for the application
- `workflows/` - LangGraph workflow definitions
- `agents/` - Agent implementations
- `tools/` - Calculator tools and utilities
- `schemas/` - Pydantic models for state management
- `config/` - Configuration management
- `utils/` - Utility functions
- `tests/` - Unit tests

## Architecture

This application uses a Sequential Workflow architecture with conditional routing:
1. Expression Parser - Extracts mathematical expression from natural language
2. Expression Validator - Validates the expression syntax
3. Calculator - Computes the result
4. Response Formatter - Formats the final response