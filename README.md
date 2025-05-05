# MCP Server + Cursor (LLM) Productivity Demo

This repository demonstrates how to use a Python-based MCP server together with a local LLM (simulated as "Cursor") to improve productivity by automating and assisting with server tasks.

## Features
- Minimal MCP server using FastAPI
- Simulated LLM (Cursor) integration
- Example workflow showing how the LLM can interact with the MCP server

## Requirements
- Python 3.8+
- pip

## Setup
```bash
pip install -r requirements.txt
```

## Running the MCP Server
```bash
python mcp_server.py
```

## Using the LLM (Cursor) Demo
In a separate terminal, run:
```bash
python cursor_llm_demo.py
```

This will show how the LLM can:
- Query the MCP server
- Automate repetitive tasks
- Provide suggestions or summaries

## File Overview
- `mcp_server.py`: The FastAPI-based MCP server
- `cursor_llm_demo.py`: Simulated LLM client interacting with the server
- `requirements.txt`: Python dependencies

## Example Output
```
[LLM] Sending request to MCP server...
[LLM] Received response: { ... }
[LLM] Task completed and summarized.
```

## What Can You Do with GitHub MCP in Daily Development?

After connecting GitHub MCP to Cursor, you can leverage it for much more than just background automation. Here's how you can see tangible, visible results and truly improve your development workflow:

### 1. Directly Experience MCP Tools in Cursor
With GitHub MCP connected, you can use natural language in Cursor to automate many development tasks, such as:

- **Automatically Create Issues/PRs**
  For example, type: "Create an issue in my repo with the content 'Test MCP tool'" and MCP will create it, returning the issue link and details.
- **Search Code/Documentation**
  For example: "Find all code snippets about 'login' in my repo." MCP will return relevant code and file paths.
- **Batch Operations**
  For example: "Replace the company name in all README files with the new name." MCP can modify and submit a PR automatically.

#### Try This:
1. In Cursor, type: "Create an issue in my repository with the content 'MCP tool test'."
2. Or: "Find all files containing 'fastapi'."

MCP will return actionable results (like issue links or code snippets) you can click and review directly.

---

### 2. Visualization Dashboard (Optional Advanced)
If you want a more visual web page, you can build a simple dashboard to display all MCP actions, such as:
- Recently created issues/PRs
- Recent code searches or batch modifications
- Details and links for each operation

You can use React, Vue, Flask, etc., to quickly build a dashboard that shows MCP's action logs and results.

---

### 3. MCP Can Proactively Push Results
MCP can also send notifications to your email, Slack, or other channels whenever it completes an operation, so you always see the results immediately.

---

### 4. Example MCP Scenarios You Can Try Now
- "How many PRs were merged this week?"
- "List all TODO comments in the repo."
- "Generate API documentation for this project."

Just type these requests in Cursor (in English or Chinese), and MCP will use GitHub tools to return real, clickable, reviewable results.

---

### Summary
- MCP is not just working in the background—it lets you drive development automation with natural language, and the results are visible and traceable.
- You can experience this directly in Cursor, or build your own visualization page.
- If you want a specific "action history page" or "results dashboard," feel free to ask for a sample front-end demo!

#### Try typing in Cursor:
> "Create an issue in my GitHub repo with the content 'MCP test'."

If you want a front-end page or a more detailed visualization solution, let us know your needs and we can help you implement it!

---
This demo is for educational purposes and can be extended for real-world productivity workflows.