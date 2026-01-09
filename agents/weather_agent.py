# weather_agent.py

"""
Weather Agent Module

This module initializes and returns a specialized Weather Agent.
The Weather Agent:
- Fetches real-time weather data for a given location
- Provides actionable clothing recommendations
- Uses the weather_tool integrated with a Gemini LLM model
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools.weather_tool import weather_tool
from prompts import WEATHER_AGENT_USER_PROMPT
from config import TEMPERATURE, GEMINI_MODEL

def get_weather_agent():
    """
    Summary:
        Initializes and returns a LangChain agent specialized for
        weather queries, capable of fetching live weather data
        and providing clothing suggestions.

    Args:
        None    

    Returns:
        Agent:
            A LangChain agent instance configured with:
            - Gemini model
            - Weather tool for real-time weather information
            - System prompt defining agent behavior and output formatting

    Raises:
        Exception:
            Raised if the agent fails to initialize or the model configuration
            is invalid.
    """
    # Initialize the Gemini language model
    model = ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        temperature=TEMPERATURE
    )

    # Create the Weather Agent with the weather tool and system prompt
    agent = create_agent(
        model=model,
        tools=[weather_tool],
        system_prompt=WEATHER_AGENT_USER_PROMPT
    )

    return agent
