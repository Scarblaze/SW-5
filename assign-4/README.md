# Assignment 4 - Multi-Step Planning Agent

## Objective
This assignment implements a **planning-based AI agent** capable of solving tasks requiring multiple sequential steps.

The agent:
- breaks the task into smaller steps
- creates an execution plan
- executes each step sequentially
- shows intermediate outputs
- returns final result

---

## Framework Used
This assignment uses **LangChain PromptTemplate** for structured task planning and decomposition.

Reason for choosing LangChain:
- clean prompt abstraction
- strong support for sequential workflows
- ideal for planning-based agents
- easy progression from previous assignments

---

## Project Structure
```bash
assignment4_multi_step_agent/
│
├── planner.py
├── executor.py
├── main.py
└── README.md
```

---

## Workflow
```text
User Query
   ↓
Task Decomposition
   ↓
Plan Creation
   ↓
Sequential Execution
   ↓
Intermediate Outputs
   ↓
Final Response
```

---

## Example Input
```text
Find the average of 5, 10, 15 and summarize the result
```

---

## Example Output
```text
Execution Plan:
- extract_numbers
- compute_average
- generate_summary

Intermediate Outputs:
numbers: [5, 10, 15]
average: 10.0
summary: The average of the given numbers is 10.0.
```

---

## Expected Learning
- Task decomposition
- Sequential reasoning
- Planning-based agents
- Intermediate observability

---

## How to Run
```bash
python main.py
```