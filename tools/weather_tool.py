import requests
import os
from langchain.tools import tool

@tool
def weather_tool(city: str) -> str:
    """Fetch weather data and suggest clothing."""
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
