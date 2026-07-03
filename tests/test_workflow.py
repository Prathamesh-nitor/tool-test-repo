"""Integration tests for calculator workflow."""

import unittest

from workflows.calculator_graph import create_calculator_graph


class TestCalculatorWorkflow(unittest.TestCase):
    """Test cases for calculator workflow."""

    def setUp(self):
        """Set up test fixtures."""
        self.app = create_calculator_graph()

    def test_simple_addition(self):
        """Test simple addition workflow."""
        result = self.app.invoke({
            "expression": "What is 25 plus 17?",
            "parsed_expression": None,
            "validation_error": None,
            "result": None,
            "formatted_response": None,
            "error": None
        })

        self.assertIsNotNone(result.get("formatted_response"))
        self.assertIsNone(result.get("error"))
        self.assertIsNotNone(result.get("result"))

    def test_complex_expression(self):
        """Test complex expression workflow."""
        result = self.app.invoke({
            "expression": "Calculate 10 times 5 minus 3",
            "parsed_expression": None,
            "validation_error": None,
            "result": None,
            "formatted_response": None,
            "error": None
        })

        self.assertIsNotNone(result.get("formatted_response"))
        self.assertIsNone(result.get("error"))
        self.assertIsNotNone(result.get("result"))

    def test_division(self):
        """Test division workflow."""
        result = self.app.invoke({
            "expression": "What's 100 divided by 4?",
            "parsed_expression": None,
            "validation_error": None,
            "result": None,
            "formatted_response": None,
            "error": None
        })

        self.assertIsNotNone(result.get("formatted_response"))
        self.assertIsNone(result.get("error"))
        self.assertEqual(result.get("result"), 25.0)


if __name__ == "__main__":
    unittest.main()