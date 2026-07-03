"""Main entry point for the calculator application."""

import sys
from typing import Optional

from workflows.calculator_graph import create_calculator_graph
from utils.logger import setup_logger

logger = setup_logger(__name__)


def run_calculator(expression: str) -> Optional[str]:
    """
    Run the calculator with the given expression.

    Args:
        expression: Natural language arithmetic expression

    Returns:
        Optional[str]: Formatted result or None if error
    """
    try:
        logger.info(f"Processing expression: {expression}")

        app = create_calculator_graph()

        result = app.invoke({
            "expression": expression,
            "parsed_expression": None,
            "validation_error": None,
            "result": None,
            "formatted_response": None,
            "error": None
        })

        formatted_response = result.get("formatted_response")
        logger.info(f"Final response: {formatted_response}")

        return formatted_response

    except Exception as e:
        logger.error(f"Error running calculator: {str(e)}")
        return f"Error: {str(e)}"


def main():
    """Main function for interactive calculator."""
    print("=" * 60)
    print("LangGraph Calculator Application")
    print("=" * 60)
    print("\nEnter arithmetic expressions in natural language.")
    print("Examples:")
    print("  - What is 25 plus 17?")
    print("  - Calculate 10 times 5 minus 3")
    print("  - What's 100 divided by 4?")
    print("  - 2 to the power of 8")
    print("\nType 'quit' or 'exit' to stop.\n")

    while True:
        try:
            expression = input("Expression: ").strip()

            if expression.lower() in ["quit", "exit", "q"]:
                print("\nGoodbye!")
                break

            if not expression:
                print("Please enter an expression.\n")
                continue

            result = run_calculator(expression)
            print(f"\n{result}\n")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    main()