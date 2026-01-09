# core_agent.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools.math_tool import math_tool
from tools.text_analyzer import text_analyzer
from tools.date_utility import date_utility
from prompts import CORE_AGENT_SYSTEM_PROMPT
from cred import load_credentials
from config import GEMINI_MODEL, TEMPERATURE

tools = [math_tool, text_analyzer, date_utility]

def get_core_agent():
    """
    Initializes and returns a production-ready LangChain agent
    using Google Gemini with multi-tool support.
    """
    # Load credentials
    load_credentials()

    # Initialize Gemini model
    model = ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        temperature=TEMPERATURE
    )

    # Create agent
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=CORE_AGENT_SYSTEM_PROMPT
    )

    return agent
