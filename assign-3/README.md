# Assignment 3 - LLM Based Agent

## Objective
This assignment implements an **LLM-driven AI agent** that improves decision-making by using a language model for tool selection.

The agent:
- accepts natural language input
- uses an LLM (Gemini API / simulated fallback) to decide the best tool
- executes the selected tool
- returns the response
- stores execution logs

---

## Features
- LLM-based tool selection
- Calculator tool
- Weather tool
- Text summarizer tool
- Execution logging
- Fallback logic if API quota is unavailable

---

## Project Structure
```bash
assignment3_llm_based_agent/
│
├── tools.py
├── llm_agent.py
├── main.py
├── logs.txt
└── README.md
```

---

## Workflow
```text
User Query
   ↓
LLM Decision
   ↓
Tool Selection
   ↓
Tool Execution
   ↓
Response
   ↓
Logging
```

---

## Example Input
```text
calculate 5 + 7
weather Mumbai
summarize AI agents use tools and reasoning
```

---

## Expected Learning
- Prompt-based decision making
- LLM integration
- AI-driven tool selection
- Logging and observability

---

## How to Run
```bash
python main.py
```

---

## Notes
If Gemini API quota is exhausted, the system uses a **simulated semantic fallback reasoning layer** to maintain agent reliability.