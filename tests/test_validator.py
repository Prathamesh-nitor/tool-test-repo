"""Unit tests for expression validator."""

import unittest

from tools.expression_validator import ExpressionValidator


class TestExpressionValidator(unittest.TestCase):
    """Test cases for ExpressionValidator."""

    def setUp(self):
        """Set up test fixtures."""
        self.validator = ExpressionValidator()

    def test_valid_addition(self):
        """Test valid addition expression."""
        is_valid, error = self.validator.validate("25 + 17")
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_valid_complex_expression(self):
        """Test valid complex expression."""
        is_valid, error = self.validator.validate("(10 + 5) * 2 - 3")
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_valid_exponentiation(self):
        """Test valid exponentiation expression."""
        is_valid, error = self.validator.validate("2 ** 8")
        self.assertTrue(is_valid)
        self.assertIsNone(error)

    def test_empty_expression(self):
        """Test empty expression."""
        is_valid, error = self.validator.validate("")
        self.assertFalse(is_valid)
        self.assertIsNotNone(error)

    def test_invalid_characters(self):
        """Test expression with invalid characters."""
        is_valid, error = self.validator.validate("25 + abc")
        self.assertFalse(is_valid)
        self.assertIsNotNone(error)

    def test_syntax_error(self):
        """Test expression with syntax error."""
        is_valid, error = self.validator.validate("25 + + 17")
        self.assertFalse(is_valid)
        self.assertIsNotNone(error)

    def test_unbalanced_parentheses(self):
        """Test expression with unbalanced parentheses."""
        is_valid, error = self.validator.validate("(10 + 5")
        self.assertFalse(is_valid)
        self.assertIsNotNone(error)


if __name__ == "__main__":
    unittest.main()