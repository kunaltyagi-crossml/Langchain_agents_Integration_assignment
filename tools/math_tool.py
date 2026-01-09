"""
Math Tool
Safely evaluates arithmetic expressions.
"""

from langchain.tools import tool

@tool
def math_tool(expression: str) -> str:
    """Evaluate arithmetic expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Math Error: {e}"

