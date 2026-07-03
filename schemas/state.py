"""State schemas for the calculator workflow."""

from typing import Optional, TypedDict


class CalculatorState(TypedDict):
    """
    State for the calculator workflow.

    Attributes:
        expression: The original user input expression
        parsed_expression: The extracted mathematical expression
        validation_error: Error message if validation fails
        result: The calculated result
        formatted_response: The final formatted response to the user
        error: Any error that occurred during processing
    """

    expression: str
    parsed_expression: Optional[str]
    validation_error: Optional[str]
    result: Optional[float]
    formatted_response: Optional[str]
    error: Optional[str]