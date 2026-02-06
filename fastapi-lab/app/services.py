from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_tasks()

    def create_task(self, task_in: TaskCreate):
        return self.repo.create_task(task_in)