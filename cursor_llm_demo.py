import requests
import time

def llm_summarize(response):
    # Simulate LLM summarization
    return f"Summary: {response}"

def main():
    print("[LLM] Sending request to MCP server for status...")
    status = requests.get("http://127.0.0.1:8000/status").json()
    print(f"[LLM] Received response: {status}")
    print("[LLM] Deciding to run a task based on status...")
    time.sleep(1)
    result = requests.post("http://127.0.0.1:8000/run-task").json()
    print(f"[LLM] Received response: {result}")
    summary = llm_summarize(result)
    print(f"[LLM] Task completed and summarized: {summary}")

if __name__ == "__main__":
    main()