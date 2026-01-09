import os
from dotenv import load_dotenv

def load_credentials():
    load_dotenv()

    if not os.getenv("GEMINI_API_KEY",""):
        raise EnvironmentError("GEMINI_API_KEY missing in .env")

    if not os.getenv("WEATHER_API_KEY"):
        raise EnvironmentError("WEATHER_API_KEY missing in .env")
