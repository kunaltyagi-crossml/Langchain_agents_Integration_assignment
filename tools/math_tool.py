# math_tool.py
# -------------
# Safe arithmetic calculation tool for LangChain agents.
#
# This module defines:
#   - math_calculator: Safely evaluates arithmetic expressions using AST parsing.
#
# Purpose:
#   Ensures that math expressions are evaluated securely, errors are handled gracefully,
#   and results are returned in a human-friendly string format.

import ast
import operator as op
from langchain_core.tools import tool
from logger_config import setup_logger

# -----------------------
# Logger setup
# -----------------------
logger = setup_logger(__name__)

# -----------------------
# Supported operators
# -----------------------
OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
}

# -----------------------
# Internal AST evaluator
# -----------------------
def _eval_expr(node):
    """
    Recursively evaluates a restricted AST node representing an arithmetic expression.

    Args:
        node: AST node (ast.Constant, ast.BinOp).

    Returns:
        Numeric result of the expression.
    """
    logger.debug(f"Evaluating AST node: {type(node).__name__}")
    if isinstance(node, ast.Constant):
        return node.n
    if isinstance(node, ast.BinOp):
        return OPERATORS[type(node.op)](
            _eval_expr(node.left),
            _eval_expr(node.right)
        )
    logger.error(f"Invalid expression node type: {type(node).__name__}")
    raise ValueError("Invalid expression node")

# -----------------------
# Math calculator tool
# -----------------------
@tool
def math_calculator(expression: str) -> str:
    """
    Safely evaluates a basic arithmetic expression.

    Args:
        expression (str): Arithmetic expression (e.g., "(234 * 12) + 98").

    Returns:
        str: Formatted result "Result: <value>" or error message.
    """
    logger.info(f"[TOOL CALL] math_calculator invoked with expression: {expression}")
    try:
        tree = ast.parse(expression, mode="eval")
        result = _eval_expr(tree.body)
        logger.info(f"[TOOL SUCCESS] Math calculation result: {result}")
        return f"Result: {result}"
    except Exception as e:
        logger.error(f"[TOOL ERROR] Math calculation failed: {str(e)}", exc_info=True)
        return f"Error evaluating expression: {str(e)}"
