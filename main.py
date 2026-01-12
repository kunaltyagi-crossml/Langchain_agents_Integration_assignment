# main.py
# -------
# Demonstrates usage of two LangChain agents:
# 1. Core Agent - Handles arithmetic, date computations, and text analysis
# 2. Weather Agent - Fetches live weather data and provides clothing recommendations
#
# Runs example queries through each agent and prints human-readable responses.

from agents.core_agent import invoke_core_agent_with_memory
from agents.weather_agent import invoke_weather_agent_with_memory
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
    # Define user ID for memory persistence
    user_id = "default_user"

    # Core agent example queries
    core_queries = [
        "What will be the date 45 days from today?",
        "Analyze this paragraph: I am very happy with the excellent service.",
        "What is (234 * 12) + 98?"
    ]

    for query in core_queries:
        print("\nUser:", query)
        # Invoke core agent with memory
        response = invoke_core_agent_with_memory(
            messages={"messages": [HumanMessage(content=query)]},
            user_id=user_id
        )

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
    weather_response = invoke_weather_agent_with_memory(
        messages={"messages": [HumanMessage(content=weather_query)]},
        user_id=user_id
    )

    print("\n--- Weather Agent Response ---")
    if "messages" in weather_response:
        print(weather_response["messages"][-1].content)
    else:
        # fallback if messages key is missing
        print(weather_response)


if __name__ == "__main__":
    main()