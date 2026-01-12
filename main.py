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
from prompts import user_query_1, user_query_2, user_query_3, user_query_4


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

    # Core agent example queries - using prompts from prompts.py
    core_queries = [
        user_query_1.content,  # "What will be the date 45 days from today?"
        user_query_2.content,  # "Analyze this paragraph: I am very happy with the excellent service."
        user_query_3.content   # "What is (234 * 12) + 98?"
    ]

    print("="*60)
    print("CORE AGENT DEMONSTRATIONS")
    print("="*60)

    for query in core_queries:
        print("\n" + "-"*60)
        print("User:", query)
        print("-"*60)
        
        # Invoke core agent with memory
        response = invoke_core_agent_with_memory(
            messages={"messages": [HumanMessage(content=query)]},
            user_id=user_id
        )

        print("\n--- Core Agent Response ---")
        # Access the last message content
        if "messages" in response:
            print(response["messages"][-1].content)
        else:
            # fallback if messages key is missing
            print(response)

    # Weather agent example - using prompt from prompts.py
    weather_query = user_query_4.content  # "What is today's weather in Chandigarh and suggest clothing accordingly?"
    
    print("\n" + "="*60)
    print("WEATHER AGENT DEMONSTRATION")
    print("="*60)
    print("\n" + "-"*60)
    print("User:", weather_query)
    print("-"*60)
    
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

    print("\n" + "="*60)
    print("ALL DEMONSTRATIONS COMPLETED")
    print("="*60)


if __name__ == "__main__":
    main()