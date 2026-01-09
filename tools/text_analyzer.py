"""
Text Analyzer Tool
Provides word count, character count, and basic sentiment.
"""

from langchain.tools import tool

@tool
def text_analyzer(text: str) -> dict:
    """Analyze text statistics and sentiment."""
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
