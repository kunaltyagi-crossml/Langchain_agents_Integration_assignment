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
from logger_config import setup_logger

# Initialize logger for this module
logger = setup_logger(__name__)

logger.info("Starting credential loading process")

# Load variables from .env file into environment
load_dotenv()
logger.debug(".env file loaded successfully")

# -----------------------------
# Read API Keys from Environment
# -----------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
MEM0_API_KEY = os.getenv("MEM0_API_KEY", "")

logger.debug(f"GEMINI_API_KEY present: {bool(GEMINI_API_KEY)}")
logger.debug(f"WEATHER_API_KEY present: {bool(WEATHER_API_KEY)}")
logger.debug(f"MEM0_API_KEY present: {bool(MEM0_API_KEY)}")

# -----------------------------
# Validate API Keys
# -----------------------------
if not GEMINI_API_KEY:
    logger.critical("GEMINI_API_KEY not found in .env file")
    raise EnvironmentError("GEMINI_API_KEY missing in .env")

if not WEATHER_API_KEY:
    logger.critical("WEATHER_API_KEY not found in .env file")
    raise EnvironmentError("WEATHER_API_KEY missing in .env")

if not MEM0_API_KEY:
    logger.critical("MEM0_API_KEY not found in .env file")
    raise EnvironmentError("MEM0_API_KEY missing in .env")

logger.info("All required API keys validated successfully")

# -----------------------------
# Memory Configuration
# -----------------------------
# User ID for mem0 persistence (can be dynamic later)
USER_ID = "Kunal Tyagi"
