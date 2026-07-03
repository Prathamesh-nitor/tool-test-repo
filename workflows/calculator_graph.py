"""LangGraph workflow definition for calculator application."""

from typing import Literal

from langgraph.graph import StateGraph, END

from agents.calculator_agent import CalculatorAgent
from schemas.state import CalculatorState
from utils.logger import setup_logger

logger = setup_logger(__name__)


def create_calculator_graph():
    """
    Create and compile the calculator LangGraph workflow.

    Returns:
        CompiledGraph: Compiled LangGraph workflow
    """
    logger.info("Creating calculator graph")

    agent = CalculatorAgent()

    workflow = StateGraph(CalculatorState)

    workflow.add_node("parse_expression", agent.parse_expression)
    workflow.add_node("validate_expression", agent.validate_expression)
    workflow.add_node("calculate_result", agent.calculate_result)
    workflow.add_node("format_response", agent.format_response)

    workflow.set_entry_point("parse_expression")

    def should_continue_after_parse(state: CalculatorState) -> Literal["validate_expression", "format_response"]:
        """Determine next node after parsing."""
        if state.get("error"):
            return "format_response"
        return "validate_expression"

    def should_continue_after_validate(state: CalculatorState) -> Literal["calculate_result", "format_response"]:
        """Determine next node after validation."""
        if state.get("error"):
            return "format_response"
        return "calculate_result"

    workflow.add_conditional_edges(
        "parse_expression",
        should_continue_after_parse,
        {
            "validate_expression": "validate_expression",
            "format_response": "format_response"
        }
    )

    workflow.add_conditional_edges(
        "validate_expression",
        should_continue_after_validate,
        {
            "calculate_result": "calculate_result",
            "format_response": "format_response"
        }
    )

    workflow.add_edge("calculate_result", "format_response")
    workflow.add_edge("format_response", END)

    app = workflow.compile()

    logger.info("Calculator graph created successfully")
    return app