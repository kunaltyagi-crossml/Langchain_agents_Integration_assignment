# weather_agent.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools.weather_tool import weather_tool
from prompts import WEATHER_AGENT_USER_PROMPT
from config import TEMPERATURE, GEMINI_MODEL

def get_weather_agent():
    """
    Initializes a LangChain agent specialized for weather queries
    using Google Gemini and the weather tool.
    """
    # Initialize Gemini model
    model = ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        temperature=TEMPERATURE
    )

    # Create agent
    agent = create_agent(
        model=model,
        tools=[weather_tool],
        system_prompt=WEATHER_AGENT_USER_PROMPT
    )

    return agent
