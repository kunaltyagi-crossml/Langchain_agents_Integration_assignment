"""
main.py

This script demonstrates the usage of two LangChain agents:
1. Core Agent - Handles arithmetic, date computations, and text analysis
2. Weather Agent - Fetches live weather data and provides clothing recommendations

It runs example queries through each agent and prints the human-readable responses.
"""

from agents.core_agent import get_core_agent
from agents.weather_agent import get_weather_agent
from langchain_core.messages import HumanMessage

def main():
    """
    Summary:
        Initializes the Core and Weather agents and runs example queries
        through each agent, printing the results in a human-friendly format.

    Args:
        None

    Returns:
        None
            Prints agent responses directly to the console.

    Raises:
        Exception:
            Any exceptions raised during agent initialization or query invocation
            will propagate and halt execution.
    """
    # Initialize agents
    core_agent = get_core_agent()
    weather_agent = get_weather_agent()

    # Core agent example queries

    core_queries = [
        "What will be the date 45 days from today?",
        "Analyze this paragraph: I am very happy with the excellent service.",
        "What is (234 * 12) + 98?"
    ]

    for query in core_queries:
        print("\nUser:", query)
        # Wrap as HumanMessage
        response = core_agent.invoke({
            "messages": [HumanMessage(content=query)]
        })

        print("--- Core Agent Response ---")
        # Access the last message content
        if "messages" in response:
            print(response["messages"][-1].content)
        else:
            # fallback if messages key is missing
            print(response)

    # Weather agent example
    
    weather_query = "What is today's weather in Chandigarh and suggest clothing accordingly?"
    print("\nUser:", weather_query)
    weather_response = weather_agent.invoke({
        "messages": [HumanMessage(content=weather_query)]
    })

    print("\n--- Weather Agent Response ---")
    if "messages" in weather_response:
        print(weather_response["messages"][-1].content)
    else:
        # fallback if messages key is missing
        print(weather_response)

if __name__ == "__main__":
    main()
