from fastapi import FastAPI
from uuid import uuid4

app = FastAPI()

tasks = []


@app.get("/")
def home():
    return {"message": "Hello, fastAPI!"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(tasl: str):
    tasks.append(task)
    return {"message": "Atividade adicionada com sucesso!"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: str):
    tasks[task_id] = task
    return {"message": "Atividade ATUALIZADA com sucesso!"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    del tasks[task_id]
    return {"message": "Atividade DELETADA com sucesso"}