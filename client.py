"""config.py
---------
Google Gemini Model Client & Mem0 Initialization for LangChain Agents

This module initializes:
1. A `ChatGoogleGenerativeAI` client for Google Gemini with controlled
   temperature and output length.
2. A `MemoryClient` (Mem0) for persistent memory across conversations.

Purpose:
- Provide a reusable model instance for all agen
- Configure Mem0 for storing and retrieving user memories
- Centralize logging for initialization steps

Configuration Notes:
- Gemini model parameters: `temperature`, `top_p`, `top_k`, `max_output_tokens`
- API keys are imported from `cred.py` and should not be stored in source control
- Mem0 requires `memo_api_key` for authentication
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from mem0 import MemoryClient
from cred import gemini_api_key, memo_api_key
from logger_config import setup_logger

# Initialize logger
logger = setup_logger(__name__)
logger.info("Initializing Gemini chat model client")

# Initialize Gemini model
try:
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        api_key=gemini_api_key,
        temperature=0.2,
        top_p=0.9,
        top_k=40,
        max_output_tokens=512
    )
    logger.info("Gemini model initialized successfully")
    logger.debug("Model config: model=gemini-2.5-flash-lite, temperature=0.2, top_p=0.9, top_k=40, max_output_tokens=512")
except Exception as e:
    logger.error(f"Failed to initialize Gemini model: {str(e)}", exc_info=True)
    raise

# Initialize Mem0 client
logger.info("Initializing Mem0")
try:
    mem0 = MemoryClient(api_key=memo_api_key)
    logger.info("Mem0 initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Mem0: {str(e)}", exc_info=True)
    raise
