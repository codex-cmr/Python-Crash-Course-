from fastapi import FastAPI
from src.controller.controller import create_task, get_tasks
from src.models.models import Task
app = FastAPI(
    title="ma premiere Application FastAPI",
    description="ToDo  Manager",
    version="0.1.0"
)

@app.get("/api/say-hallo/")
def say_hallo():
    return {
        "message": "Hello from Codex!"
    }

@app.post("/api/tasks/create/")
def create(task:Task):
    return create_task(task.title,
                       task.description)

@app.get("/api/tasks/get")
def get_all_tasks():
    return get_tasks()

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost", port=8004)

