"""Expression validator tool for validating mathematical expressions."""

import ast
import operator
import re
from typing import Optional, Tuple

from utils.logger import setup_logger

logger = setup_logger(__name__)


class ExpressionValidator:
    """Validator for mathematical expressions."""

    ALLOWED_OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def __init__(self):
        """Initialize the expression validator."""
        pass

    def validate(self, expression: str) -> Tuple[bool, Optional[str]]:
        """
        Validate a mathematical expression.

        Args:
            expression: Mathematical expression to validate

        Returns:
            Tuple[bool, Optional[str]]: (is_valid, error_message)
        """
        try:
            logger.info(f"Validating expression: {expression}")

            if not expression or not expression.strip():
                return False, "Expression is empty"

            expression = expression.strip()

            if not re.match(r'^[\d\s\+\-\*\/\(\)\.\*\*]+$', expression):
                return False, "Expression contains invalid characters"

            try:
                tree = ast.parse(expression, mode='eval')
            except SyntaxError as e:
                return False, f"Syntax error in expression: {str(e)}"

            if not self._validate_ast(tree.body):
                return False, "Expression contains disallowed operations"

            logger.info("Expression is valid")
            return True, None

        except Exception as e:
            logger.error(f"Error validating expression: {str(e)}")
            return False, f"Validation error: {str(e)}"

    def _validate_ast(self, node: ast.AST) -> bool:
        """
        Recursively validate AST nodes.

        Args:
            node: AST node to validate

        Returns:
            bool: True if node is valid, False otherwise
        """
        if isinstance(node, ast.Constant):
            return isinstance(node.value, (int, float))

        elif isinstance(node, ast.BinOp):
            return (
                type(node.op) in self.ALLOWED_OPERATORS
                and self._validate_ast(node.left)
                and self._validate_ast(node.right)
            )

        elif isinstance(node, ast.UnaryOp):
            return (
                type(node.op) in self.ALLOWED_OPERATORS
                and self._validate_ast(node.operand)
            )

        else:
            return False