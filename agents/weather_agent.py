# weather_agent.py
# ----------------
# Weather Agent with Mem0 memory integration
#
# This module provides:
#   - Weather agent for real-time city weather and clothing recommendations
#   - Memory-enhanced invocation using Mem0
#   - Persistent conversation storage

from typing import Dict
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage
from client import model, mem0
from prompts import WEATHER_AGENT_USER_PROMPT
from tools.weather_tool import weather_tool
from logger_config import setup_logger

logger = setup_logger(__name__)
logger.info("Initializing Weather Agent with Mem0 memory")

# -----------------------
# Weather tools
# -----------------------
weather_tools = [weather_tool]
logger.debug(f"Registered weather tools: {[tool.name for tool in weather_tools]}")

# -----------------------
# Memory helpers
# -----------------------
def retrieve_memories(query: str, user_id: str) -> str:
    logger.info(f"Retrieving memories for user: {user_id}")
    if len(query.strip().split()) < 3:
        return ""
    try:
        memories = mem0.search(query=query, filters={"user_id": user_id}, limit=5)
        memory_list = memories.get("results", [])
        if not memory_list:
            return ""
        serialized = "\n".join(f"- {mem['memory']}" for mem in memory_list)
        logger.info(f"Retrieved {len(memory_list)} memories")
        return serialized
    except Exception as e:
        logger.error(f"Error retrieving memories: {str(e)}", exc_info=True)
        return ""

def save_interaction(user_id: str, user_input: str, assistant_response: str):
    logger.info(f"Saving interaction to Mem0 for user: {user_id}")
    try:
        interaction = [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": assistant_response}
        ]
        result = mem0.add(interaction, user_id=user_id)
        logger.info(f"Memory saved successfully: {len(result.get('results', []))} memories added")
    except Exception as e:
        logger.error(f"Error saving interaction to Mem0: {str(e)}", exc_info=True)

# -----------------------
# Memory-enhanced agent invocation
# -----------------------
def invoke_weather_agent_with_memory(messages: Dict, user_id: str = "default_user") -> Dict:
    logger.info(f"Weather Agent invocation with memory for user: {user_id}")
    last_message = messages["messages"][-1]
    user_query = getattr(last_message, "content", str(last_message))
    memory_context = retrieve_memories(user_query, user_id)

    # Build enhanced system prompt content
    enhanced_system_content = f"""{WEATHER_AGENT_USER_PROMPT.content}

## MEMORY CONTEXT
{memory_context}

Rules:
- Use memory facts if available
- If user's name is known, use it
- Do NOT say you lack personal info if memory exists
"""

    # Create new SystemMessage with enhanced content
    enhanced_system_prompt = SystemMessage(content=enhanced_system_content)
    
    # Build the enhanced messages properly
    enhanced_messages = {"messages": [enhanced_system_prompt] + messages["messages"]}

    try:
        response = weather_agent.invoke(enhanced_messages)
        assistant_response = response["messages"][-1].content
        save_interaction(user_id, user_query, assistant_response)
        logger.info("Weather Agent invocation completed successfully")
        return response
    except Exception as e:
        logger.error(f"Failed to invoke Weather Agent with memory: {str(e)}", exc_info=True)
        raise

# -----------------------
# Initialize Weather Agent
# -----------------------
try:
    weather_agent = create_agent(model=model, tools=weather_tools, system_prompt=WEATHER_AGENT_USER_PROMPT)
    logger.info("Weather Agent created successfully")
except Exception as e:
    logger.error(f"Failed to create Weather Agent: {str(e)}", exc_info=True)
    raise