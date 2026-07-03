"""Expression parser tool for extracting mathematical expressions."""

import re
from typing import Optional

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from config.settings import get_settings
from utils.logger import setup_logger

logger = setup_logger(__name__)


class ExpressionParser:
    """Parser for extracting mathematical expressions from natural language."""

    def __init__(self):
        """Initialize the expression parser."""
        settings = get_settings()
        self.llm = ChatOpenAI(
            model=settings.model_name,
            temperature=settings.temperature,
            api_key=settings.openai_api_key
        )

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a mathematical expression parser. Your task is to extract the mathematical expression from natural language input.

Rules:
1. Convert word numbers to digits (e.g., "twenty-five" -> "25")
2. Convert operation words to symbols:
   - "plus", "add", "added to" -> +
   - "minus", "subtract", "subtracted from" -> -
   - "times", "multiplied by", "multiply" -> *
   - "divided by", "divide" -> /
   - "to the power of", "raised to", "exponent" -> **
3. Preserve parentheses for order of operations
4. Return ONLY the mathematical expression, nothing else
5. Use standard Python mathematical notation

Examples:
Input: "What is 25 plus 17?"
Output: 25 + 17

Input: "Calculate 10 times 5 minus 3"
Output: 10 * 5 - 3

Input: "What's 100 divided by 4 plus 8?"
Output: 100 / 4 + 8

Input: "2 to the power of 8"
Output: 2 ** 8"""),
            ("human", "{expression}")
        ])

    def parse(self, expression: str) -> Optional[str]:
        """
        Parse natural language expression to mathematical notation.

        Args:
            expression: Natural language expression

        Returns:
            Optional[str]: Parsed mathematical expression or None if parsing fails
        """
        try:
            logger.info(f"Parsing expression: {expression}")

            chain = self.prompt | self.llm
            response = chain.invoke({"expression": expression})
            parsed = response.content.strip()

            parsed = re.sub(r'\s+', ' ', parsed)

            logger.info(f"Parsed expression: {parsed}")
            return parsed

        except Exception as e:
            logger.error(f"Error parsing expression: {str(e)}")
            return None