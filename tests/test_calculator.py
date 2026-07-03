"""Unit tests for calculator tool."""

import unittest

from tools.calculator import CalculatorTool


class TestCalculatorTool(unittest.TestCase):
    """Test cases for CalculatorTool."""

    def setUp(self):
        """Set up test fixtures."""
        self.calculator = CalculatorTool()

    def test_addition(self):
        """Test addition operation."""
        result, error = self.calculator.calculate("25 + 17")
        self.assertIsNone(error)
        self.assertEqual(result, 42.0)

    def test_subtraction(self):
        """Test subtraction operation."""
        result, error = self.calculator.calculate("50 - 20")
        self.assertIsNone(error)
        self.assertEqual(result, 30.0)

    def test_multiplication(self):
        """Test multiplication operation."""
        result, error = self.calculator.calculate("10 * 5")
        self.assertIsNone(error)
        self.assertEqual(result, 50.0)

    def test_division(self):
        """Test division operation."""
        result, error = self.calculator.calculate("100 / 4")
        self.assertIsNone(error)
        self.assertEqual(result, 25.0)

    def test_exponentiation(self):
        """Test exponentiation operation."""
        result, error = self.calculator.calculate("2 ** 8")
        self.assertIsNone(error)
        self.assertEqual(result, 256.0)

    def test_complex_expression(self):
        """Test complex expression with multiple operations."""
        result, error = self.calculator.calculate("(10 + 5) * 2 - 3")
        self.assertIsNone(error)
        self.assertEqual(result, 27.0)

    def test_division_by_zero(self):
        """Test division by zero error handling."""
        result, error = self.calculator.calculate("10 / 0")
        self.assertIsNone(result)
        self.assertIsNotNone(error)
        self.assertIn("Division by zero", error)

    def test_negative_numbers(self):
        """Test negative numbers."""
        result, error = self.calculator.calculate("-5 + 10")
        self.assertIsNone(error)
        self.assertEqual(result, 5.0)


if __name__ == "__main__":
    unittest.main()