"""
text_analyzer_tool.py

Provides word count, character count, and basic sentiment.
"""
from langchain.tools import tool

@tool
def text_analyzer(text: str) -> dict:
    """
    Summary:
        Analyzes the given text to compute basic statistics and determine
        overall sentiment using simple keyword-based rules.

    Args:
        text (str):
            The input text to be analyzed.

    Returns:
        dict:
            A dictionary containing:
            - word_count (int): Total number of words in the text
            - character_count (int): Total number of characters in the text
            - sentiment (str): Overall sentiment classification
              ("Positive", "Negative", or "Neutral")

        In case of failure, the dictionary contains:
            - error (str): Description of the encountered error

    Raises:
        Exception:
            Raised when an unexpected error occurs during text processing.
    """
    try:
        word_count = len(text.split())
        char_count = len(text)

        positive = ["good", "great", "happy", "excellent"]
        negative = ["bad", "sad", "poor", "terrible"]

        text_lower = text.lower()
        pos = sum(word in text_lower for word in positive)
        neg = sum(word in text_lower for word in negative)

        sentiment = "Neutral"
        if pos > neg:
            sentiment = "Positive"
        elif neg > pos:
            sentiment = "Negative"

        return {
            "word_count": word_count,
            "character_count": char_count,
            "sentiment": sentiment
        }
    except Exception as e:
        return {"error": str(e)}
