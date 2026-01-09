# Custom LangChain Multi-Tool Agent Project

This project demonstrates how to build **tool-enabled LLM agents** using **LangChain** and **Google Gemini API**, with support for **custom tools**, **multi-tool reasoning**, and **external API integration**.

---

## 🚀 Project Overview

The project is divided into **4 parts**:

1. **Part 1 – Custom Tools**
   - **Math Tool:** Evaluate arithmetic expressions.
   - **Text Analyzer Tool:** Calculate word count, character count, and sentiment.
   - **Date Utility Tool:** Compute the date after N days from today.

2. **Part 2 – LLM + Tool Integration**
   - Integrates Gemini LLM with tools.
   - The LLM automatically selects the correct tool.
   - Example queries:  
     - `"What is (234 * 12) + 98?"`  
     - `"Analyze this paragraph and summarize the sentiment."`

3. **Part 3 – Multi-Tool Sequential Agent**
   - The agent can call multiple tools in sequence.
   - Example query:  
     `"Calculate total cost for 3 items priced at 499 each and delivery date in 7 days."`
   - Logs intermediate steps and combines results.

4. **Part 4 – External API Tool**
   - **Weather Tool:** Fetches live weather using OpenWeatherMap API.
   - Provides human-friendly clothing recommendations.
   - Example query:  
     `"What is today’s weather in Chandigarh and suggest clothing accordingly?"`

---
## ⚙️ Setup Instructions
## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Langchain_Tools_Integration
2. Create and activate a virtual environment (recommended)
bash
Copy code
python3 -m venv myvenv
source myvenv/bin/activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Set up environment variables
Create a file named .env in the root directory of this project and add your API keys:

bash
Copy code
WEATHER_API_KEY=your_weather_api_key_here
Usage
1. Core Agent
The Core Agent supports:

Mathematical calculations

Date computations

Text analysis (word count, sentiment)

Multi-step tool reasoning

Run the application:

bash
Copy code
python3 main.py
Example Queries:
What is (234 * 12) + 98?

What will be the date 45 days from today?

Analyze this paragraph: I am very happy with the excellent service.

2. Weather Agent
The Weather Agent:

Fetches live weather data

Suggests clothing based on temperature and conditions

Example query:

What is today's weather in Chandigarh and suggest clothing accordingly?

The Weather Agent is invoked automatically via main.py.

How It Works
Agents receive user input as HumanMessage

System behavior is governed by detailed prompts in prompts.py

Tools are selected dynamically based on query type

Tool outputs are treated as authoritative

Final responses are human-friendly and actionable

Learning Outcomes
Understand multi-agent architecture using LangChain

Learn structured tool-based reasoning

Design strict system prompts with DOs and DON'Ts

Avoid hallucinations using tool enforcement

Handle Pydantic validation and message schemas

Build production-ready LLM agent workflows

Future Enhancements
Persistent memory integration

Additional external APIs (currency, news)

Web or Streamlit-based UI

Enhanced logging and monitoring




