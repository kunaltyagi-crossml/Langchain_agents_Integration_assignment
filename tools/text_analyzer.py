# text_analyzer_tool.py
# ---------------------
# Text analysis tool for LangChain agents.
#
# This module defines:
#   - text_analyzer: Computes word count, character count, and basic sentiment.
#
# Purpose:
#   Provides structured analysis of text input and returns human-friendly results,
#   handling errors gracefully.

from langchain.tools import tool
from logger_config import setup_logger

# -----------------------
# Logger setup
# -----------------------
logger = setup_logger(__name__)

# -----------------------
# Text analyzer tool
# -----------------------
@tool
def text_analyzer(text: str) -> dict:
    """
    Analyzes the given text to compute basic statistics and sentiment.

    Args:
        text (str): Input text to analyze.

    Returns:
        dict:
            - word_count (int): Number of words in the text
            - character_count (int): Number of characters in the text
            - sentiment (str): "Positive", "Negative", or "Neutral"
        On error:
            - {"error": "<description>"}
    """
    logger.info(f"[TOOL CALL] text_analyzer invoked with text length: {len(text)}")
    try:
        word_count = len(text.split())
        char_count = len(text)

        positive_keywords = ["good", "great", "happy", "excellent"]
        negative_keywords = ["bad", "sad", "poor", "terrible"]

        text_lower = text.lower()
        pos = sum(word in text_lower for word in positive_keywords)
        neg = sum(word in text_lower for word in negative_keywords)

        sentiment = "Neutral"
        if pos > neg:
            sentiment = "Positive"
        elif neg > pos:
            sentiment = "Negative"

        result = {
            "word_count": word_count,
            "character_count": char_count,
            "sentiment": sentiment
        }

        logger.info(f"[TOOL SUCCESS] Text analysis complete: {result}")
        return result

    except Exception as e:
        logger.error(f"[TOOL ERROR] Text analysis failed: {str(e)}", exc_info=True)
        return {"error": str(e)}
