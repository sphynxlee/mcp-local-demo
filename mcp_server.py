from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/status")
def get_status():
    return {"status": "MCP server is running", "tasks": ["task1", "task2"]}

@app.post("/run-task")
def run_task(request: Request):
    # In a real server, parse and run the task
    return JSONResponse({"result": "Task executed successfully"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("mcp_server:app", host="127.0.0.1", port=8000, reload=True)