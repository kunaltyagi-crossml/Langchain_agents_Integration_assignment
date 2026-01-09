"""
Date Utility Tool
Calculates future dates.
"""

from langchain.tools import tool
from datetime import datetime, timedelta

@tool
def date_utility(days: int) -> str:
    """
    Summary:
        Computes the future date by adding a specified number of days
        to today's date and returns it in YYYY-MM-DD format.

    Args:
        days (int):
            The number of days to add to the current date. Can be positive
            or zero. Negative values are handled but will compute a past date.

    Returns:
        str:
            A string representing the future date in "YYYY-MM-DD" format.

        In case of failure:
            A formatted error message describing the issue.

    Raises:
        Exception:
            Raised if the input is invalid or an unexpected error occurs
            during date computation.
    """
    try:
        future_date = datetime.today() + timedelta(days=days)
        return future_date.strftime("%Y-%m-%d")
    except Exception as e:
        return f"Date Error: {e}"
