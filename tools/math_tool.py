"""
math_tool.py

Safely evaluates arithmetic expressions.
"""
from langchain.tools import tool

@tool
def math_tool(expression: str) -> str:
    """
    Summary:
        Evaluates a user-provided arithmetic expression and returns
        the computed result as a formatted string.

    Args:
        expression (str):
            A valid arithmetic expression represented as a string.
            Example: "234 * 12 + 98"

    Returns:
        str:
            A formatted string containing the evaluated result.
            Example: "Result: 2906"

        In case of failure:
            A formatted error message describing the issue.

    Raises:
        Exception:
            Raised when the expression is invalid or cannot be evaluated.
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Math Error: {e}"
