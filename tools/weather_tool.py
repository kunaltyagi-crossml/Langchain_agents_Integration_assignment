# weather_tool.py
# ----------------
# Weather tool for LangChain agents.
#
# This module defines:
#   - weather_tool: Fetches live weather data and provides human-friendly summaries
#                   including temperature, description, and clothing recommendations.
#
# Purpose:
#   Enables a Weather Agent to provide actionable weather advice within a multi-agent LLM system.
#   Handles API errors gracefully and returns structured, readable results.

import os
import requests
from langchain.tools import tool
from logger_config import setup_logger

# -----------------------
# Logger setup
# -----------------------
logger = setup_logger(__name__)

# -----------------------
# Weather tool
# -----------------------
@tool
def weather_tool(city: str) -> str:
    """
    Fetches real-time weather data for a given city and provides clothing recommendations.

    Args:
        city (str): Name of the city for which weather information is requested.

    Returns:
        str: Human-readable summary containing:
            - City name
            - Current temperature in Celsius
            - Weather description
            - Suggested clothing recommendation
        On error: returns "Weather Error: <description>"
    """
    logger.info(f"[TOOL CALL] weather_tool invoked for city: {city}")
    try:
        api_key = os.getenv("WEATHER_API_KEY")
        if not api_key:
            raise ValueError("WEATHER_API_KEY environment variable not set.")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        logger.debug(f"Making API request to OpenWeatherMap for city: {city}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") != 200:
            message = data.get("message", "Unknown error")
            logger.error(f"[TOOL ERROR] API returned error for city {city}: {message}")
            return f"Error: {message}"

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        # Clothing recommendation based on temperature
        if temp >= 30:
            clothing = "Wear light cotton clothes."
        elif temp >= 20:
            clothing = "Light clothing with a jacket."
        elif temp >= 10:
            clothing = "Wear warm clothes."
        else:
            clothing = "Wear heavy winter clothing."

        result = f"{city}: {temp}°C, {desc}. {clothing}"
        logger.info(f"[TOOL SUCCESS] Weather data retrieved: {result}")
        return result

    except Exception as e:
        logger.error(f"[TOOL ERROR] Weather tool failed: {str(e)}", exc_info=True)
        return f"Weather Error: {e}"
