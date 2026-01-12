# Custom LangChain Multi-Tool Agent Project

This project demonstrates how to build **tool-enabled LLM agents** using **LangChain** and **Google Gemini API**, with support for **custom tools**, **multi-tool reasoning**, **external API integration**, and **persistent memory using Mem0**.

---

## 🚀 Project Overview

The project is divided into **5 parts**:

1. #### Part 1 – Custom Tools**
   - **Math Tool:** Evaluate arithmetic expressions.
   - **Text Analyzer Tool:** Calculate word count, character count, and sentiment.
   - **Date Utility Tool:** Compute the date after N days from today.

2. #### Part 2 – LLM + Tool Integration**
   - Integrates Gemini LLM with tools.
   - The LLM automatically selects the correct tool.
   - Example queries:  
     - `"What is (234 * 12) + 98?"`  
     - `"Analyze this paragraph and summarize the sentiment."`

3. #### Part 3 – Multi-Tool Sequential Agent**
   - The agent can call multiple tools in sequence.
   - Example query:  
     `"Calculate total cost for 3 items priced at 499 each and delivery date in 7 days."`
   - Logs intermediate steps and combines results.

4. #### Part 4 – External API Tool**
   - **Weather Tool:** Fetches live weather using OpenWeatherMap API.
   - Provides human-friendly clothing recommendations.
   - Example query:  
     `"What is today's weather in Chandigarh and suggest clothing accordingly?"`

5. #### Part 5 – Mem0 Memory Integration**
   - **Persistent Memory:** Stores and retrieves conversation history using Mem0.
   - **Context-Aware Responses:** Agents remember user preferences and past interactions.
   - **User-Specific Memory:** Each user has isolated memory with `user_id` filtering.
   - Example: If user shares their name, agents will use it in future conversations.

---
## ⚙️ Setup Instructions

#### 1. Clone the repository

      git clone https://github.com/kunaltyagi-crossml/LLM-Prompting-Assignment.git
      cd Langchain_Tools_Integration

#### 2. Create and activate a virtual environment (recommended)

      python3 -m venv myvenv
      source myvenv/bin/activate
      
#### 3. Install dependencies

      pip install -r requirements.txt
      
#### 4. Set up environment variables
Create a file named .env in the root directory of this project and add your API keys:

      WEATHER_API_KEY=your_weather_api_key_here
      GEMINI_API_KEY=your_gemini_api_key_here
      MEM0_API_KEY=your_mem0_api_key_here

## Usage
#### 1. Core Agent
The Core Agent supports:
- Mathematical calculations
- Date computations
- Text analysis (word count, sentiment)
- Multi-step tool reasoning
- **Memory-enhanced conversations**

Run the application:

      python3 main.py
      
Example Queries:

- What is (234 * 12) + 98?
- What will be the date 45 days from today?
- Analyze this paragraph: I am very happy with the excellent service.
- My name is John (agent will remember this for future conversations)

#### 2. Weather Agent
The Weather Agent:

- Fetches live weather data
- Suggests clothing based on temperature and conditions
- **Remembers user's location preferences**

Example query:

- What is today's weather in Chandigarh and suggest clothing accordingly?

The Weather Agent is invoked automatically via main.py.

#### How It Works

- Agents receive user input as HumanMessage
- System behavior is governed by detailed prompts in prompts.py
- Tools are selected dynamically based on query type
- **Mem0 retrieves relevant memories** before processing each query
- Tool outputs are treated as authoritative
- **Conversations are saved to Mem0** for future context
- Final responses are human-friendly and actionable

#### Memory System Features

- **Automatic Memory Retrieval:** Relevant past conversations are fetched based on query similarity
- **User-Specific Storage:** Each user's memory is isolated using `user_id`
- **Persistent Context:** Agent remembers user preferences, names, and past interactions
- **Smart Memory Search:** Only queries with 3+ words trigger memory lookup (optimization)

#### Learning Outcomes

- Understand multi-agent architecture using LangChain
- Learn structured tool-based reasoning
- Design strict system prompts with DOs and DON'Ts
- Avoid hallucinations using tool enforcement
- Handle Pydantic validation and message schemas
- **Implement persistent memory with Mem0**
- **Build context-aware conversational agents**
- Build production-ready LLM agent workflows

#### Future Enhancements 

- Additional external APIs (currency, news)
- Web or Streamlit-based UI
- Enhanced logging and monitoring
- Multi-user session management