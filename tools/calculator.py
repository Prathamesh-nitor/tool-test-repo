"""Calculator tool for evaluating mathematical expressions."""

import ast
import operator
from typing import Optional, Tuple

from utils.logger import setup_logger

logger = setup_logger(__name__)


class CalculatorTool:
    """Tool for safely evaluating mathematical expressions."""

    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def __init__(self):
        """Initialize the calculator tool."""
        pass

    def calculate(self, expression: str) -> Tuple[Optional[float], Optional[str]]:
        """
        Safely evaluate a mathematical expression.

        Args:
            expression: Mathematical expression to evaluate

        Returns:
            Tuple[Optional[float], Optional[str]]: (result, error_message)
        """
        try:
            logger.info(f"Calculating expression: {expression}")

            tree = ast.parse(expression, mode='eval')
            result = self._eval_node(tree.body)

            logger.info(f"Calculation result: {result}")
            return result, None

        except ZeroDivisionError:
            error_msg = "Division by zero error"
            logger.error(error_msg)
            return None, error_msg

        except Exception as e:
            error_msg = f"Calculation error: {str(e)}"
            logger.error(error_msg)
            return None, error_msg

    def _eval_node(self, node: ast.AST) -> float:
        """
        Recursively evaluate AST nodes.

        Args:
            node: AST node to evaluate

        Returns:
            float: Evaluation result

        Raises:
            ValueError: If node type is not supported
        """
        if isinstance(node, ast.Constant):
            return float(node.value)

        elif isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            op_func = self.OPERATORS.get(type(node.op))

            if op_func is None:
                raise ValueError(f"Unsupported operator: {type(node.op)}")

            return op_func(left, right)

        elif isinstance(node, ast.UnaryOp):
            operand = self._eval_node(node.operand)
            op_func = self.OPERATORS.get(type(node.op))

            if op_func is None:
                raise ValueError(f"Unsupported operator: {type(node.op)}")

            return op_func(operand)

        else:
            raise ValueError(f"Unsupported node type: {type(node)}")