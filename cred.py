"""
cred.py
--------
This file is responsible for loading and validating
all sensitive credentials (API keys).

Best Practice:
- Credentials are NOT hardcoded
- Values are loaded from environment variables
"""

import os
from dotenv import load_dotenv

def load_credentials():
    load_dotenv()

    if not os.getenv("GEMINI_API_KEY",""):
        raise EnvironmentError("GEMINI_API_KEY missing in .env")

    if not os.getenv("WEATHER_API_KEY"):
        raise EnvironmentError("WEATHER_API_KEY missing in .env")
