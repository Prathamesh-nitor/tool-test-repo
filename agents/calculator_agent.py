"""Calculator agent for orchestrating calculation workflow."""

from typing import Dict, Any

from schemas.state import CalculatorState
from tools.calculator import CalculatorTool
from tools.expression_parser import ExpressionParser
from tools.expression_validator import ExpressionValidator
from utils.logger import setup_logger

logger = setup_logger(__name__)


class CalculatorAgent:
    """Agent for handling calculator operations."""

    def __init__(self):
        """Initialize the calculator agent."""
        self.parser = ExpressionParser()
        self.validator = ExpressionValidator()
        self.calculator = CalculatorTool()

    def parse_expression(self, state: CalculatorState) -> Dict[str, Any]:
        """
        Parse natural language expression to mathematical notation.

        Args:
            state: Current workflow state

        Returns:
            Dict[str, Any]: Updated state
        """
        logger.info("Parsing expression node")

        parsed = self.parser.parse(state["expression"])

        if parsed is None:
            return {
                "parsed_expression": None,
                "error": "Failed to parse expression"
            }

        return {
            "parsed_expression": parsed,
            "error": None
        }

    def validate_expression(self, state: CalculatorState) -> Dict[str, Any]:
        """
        Validate the parsed mathematical expression.

        Args:
            state: Current workflow state

        Returns:
            Dict[str, Any]: Updated state
        """
        logger.info("Validating expression node")

        if state.get("error"):
            return {}

        parsed_expr = state.get("parsed_expression")
        if not parsed_expr:
            return {
                "validation_error": "No expression to validate",
                "error": "No expression to validate"
            }

        is_valid, error_msg = self.validator.validate(parsed_expr)

        if not is_valid:
            return {
                "validation_error": error_msg,
                "error": error_msg
            }

        return {
            "validation_error": None
        }

    def calculate_result(self, state: CalculatorState) -> Dict[str, Any]:
        """
        Calculate the result of the expression.

        Args:
            state: Current workflow state

        Returns:
            Dict[str, Any]: Updated state
        """
        logger.info("Calculating result node")

        if state.get("error"):
            return {}

        parsed_expr = state.get("parsed_expression")
        if not parsed_expr:
            return {
                "error": "No expression to calculate"
            }

        result, error_msg = self.calculator.calculate(parsed_expr)

        if error_msg:
            return {
                "result": None,
                "error": error_msg
            }

        return {
            "result": result,
            "error": None
        }

    def format_response(self, state: CalculatorState) -> Dict[str, Any]:
        """
        Format the final response.

        Args:
            state: Current workflow state

        Returns:
            Dict[str, Any]: Updated state
        """
        logger.info("Formatting response node")

        if state.get("error"):
            formatted = f"Error: {state['error']}"
        else:
            result = state.get("result")
            parsed_expr = state.get("parsed_expression")
            formatted = f"The result of {parsed_expr} is {result}"

        return {
            "formatted_response": formatted
        }