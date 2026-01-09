"""
config.py

Initializes a Google Gemini chat model client for use with LangChain. This module
creates a `ChatGoogleGenerativeAI` instance configured for low-variance responses
and a capped output length, and exports it as `model` for reuse across the app.

Configuration notes:
- `temperature`, `top_p`, and `top_k` control sampling/creativity.
- `max_output_tokens` caps the maximum tokens in the model's response.

Security:
- Store the API key outside source control (for example via environment variables
  or a separate secrets/credentials file that is not committed).
"""



# config.py
GEMINI_MODEL = "gemini-2.5-flash-lite"
TEMPERATURE = 0
