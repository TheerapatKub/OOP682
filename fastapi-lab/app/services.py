from fastapi import HTTPException
from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        existing_task = self.repo.get_by_title(task_in.title)
        if existing_task:
            raise HTTPException(status_code=400, detail="Task title already exists")
        return self.repo.create(task_in)

    def complete_task(self, task_id: int):
        task = self.repo.get_by_id(task_id)
        if not task:
            return None
        task_in = TaskCreate(
            title=task.title,
            description=task.description,
            completed=True,
        )
        return self.repo.update(task_id, task_in)