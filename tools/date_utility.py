# date_utility_tool.py
# --------------------
# Date utility tool for LangChain agents.
#
# This module defines:
#   - date_utility: Computes future (or past) dates by adding N days to today.
#
# Purpose:
#   Provides safe computation of calendar dates, returns ISO-formatted strings,
#   and handles errors gracefully.

from langchain.tools import tool
from datetime import datetime, timedelta
from logger_config import setup_logger

# -----------------------
# Logger setup
# -----------------------
logger = setup_logger(__name__)

# -----------------------
# Date utility tool
# -----------------------
@tool
def date_utility(days: int) -> str:
    """
    Computes the future date by adding a specified number of days to today.

    Args:
        days (int): Number of days to add to today's date.
                    Positive, zero, or negative values allowed.

    Returns:
        str: Future date in "YYYY-MM-DD" format, or error message if invalid.
    """
    logger.info(f"[TOOL CALL] date_utility invoked with days: {days}")
    try:
        if not isinstance(days, int):
            raise TypeError("Days must be an integer.")
        future_date = datetime.today() + timedelta(days=days)
        result = future_date.strftime("%Y-%m-%d")
        logger.info(f"[TOOL SUCCESS] Calculated date: {result}")
        return result
    except Exception as e:
        logger.error(f"[TOOL ERROR] Date calculation failed: {str(e)}", exc_info=True)
        return f"Date Error: {e}"
