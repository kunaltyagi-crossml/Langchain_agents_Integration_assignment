"""
weather_tool.py

This module defines a LangChain tool to fetch live weather data for a given city
using the OpenWeatherMap API. It provides human-friendly summaries including
temperature, weather description, and clothing recommendations based on the
current temperature.

The tool is designed to be used by a Weather Agent within a multi-agent LLM
system built with LangChain.
"""

import requests
import os
from langchain.tools import tool

@tool
def weather_tool(city: str) -> str:
    """
    Summary:
        Fetches real-time weather data for a given city and provides
        clothing recommendations based on temperature.

    Args:
        city (str):
            Name of the city for which weather information is requested.

    Returns:
        str:
            A human-readable summary containing:
            - City name
            - Current temperature in Celsius
            - Weather description
            - Suggested clothing recommendation

    Raises:
        Exception:
            Raised when an unexpected error occurs during the API request,
            environment variable access, or response parsing.
    """
    try:
        api_key = os.getenv("WEATHER_API_KEY")

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={api_key}&units=metric"
        )

        data = requests.get(url).json()

        if data.get("cod") != 200:
            return f"Error: {data.get('message')}"

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        if temp >= 30:
            clothing = "Wear light cotton clothes."
        elif temp >= 20:
            clothing = "Light clothing with a jacket."
        elif temp >= 10:
            clothing = "Wear warm clothes."
        else:
            clothing = "Wear heavy winter clothing."

        return f"{city}: {temp}°C, {desc}. {clothing}"

    except Exception as e:
        return f"Weather Error: {e}"
