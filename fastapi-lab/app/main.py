from fastapi import FastAPI, Depends
from typing import List
from .models import Task, TaskCreate
from .repositories import task_repo, get_task_service
from .services import TaskService

app = FastAPI()
tack_repo = InmemoryTaskRepository()

# main.py

# เดิม:
# def get_task_service():
#     return TaskService(InMemoryTaskRepository())

# ใหม่ (ใช้ SQL):
def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@app.post("/tasks", response_model=Task)
def create_task(
    task: TaskCreate, 
    service: TaskService = Depends(get_task_service)
):
    return service.create_task(task)

