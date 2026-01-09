# core_agent.py

"""
Core Agent Module

This module initializes and returns the Core Agent for the project.
The Core Agent can:
- Perform arithmetic calculations
- Analyze text for word count and sentiment
- Compute future dates

It leverages:
- Gemini LLM via langchain_google_genai
- Custom tools: math_tool, text_analyzer, date_utility
- Structured system prompt from prompts.py
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools.math_tool import math_tool
from tools.text_analyzer import text_analyzer
from tools.date_utility import date_utility
from prompts import CORE_AGENT_SYSTEM_PROMPT
from cred import load_credentials
from config import GEMINI_MODEL, TEMPERATURE

# List of tools available for the Core Agent
tools = [math_tool, text_analyzer, date_utility]

def get_core_agent():
    """
    Summary:
        Initializes and returns a production-ready Core Agent capable
        of multi-tool reasoning with LangChain.

    Args:
        None    

    Returns:
        Agent:
            A LangChain agent instance configured with:
            - Gemini model
            - Core tools (math, text analysis, date utility)
            - System prompt defining agent behavior and reasoning guidelines

    Raises:
        Exception:
            Raised if credentials fail to load or agent initialization fails.
    """
    # Load API credentials from environment or config
    load_credentials()

    # Initialize the Gemini language model
    model = ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        temperature=TEMPERATURE
    )

    # Create and configure the Core Agent with tools and system prompt
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=CORE_AGENT_SYSTEM_PROMPT
    )

    return agent
