"""
Date Utility Tool
Calculates future dates.
"""

from langchain.tools import tool
from datetime import datetime, timedelta

@tool
def date_utility(days: int) -> str:
    """Return date after N days."""
    try:
        future_date = datetime.today() + timedelta(days=days)
        return future_date.strftime("%Y-%m-%d")
    except Exception as e:
        return f"Date Error: {e}"
