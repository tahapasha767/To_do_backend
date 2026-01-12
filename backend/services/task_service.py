from typing import List, Optional
from models.task import Task, TaskCreate, TaskUpdate, TaskStatus
from storage import memory


def list_tasks(status: Optional[TaskStatus] = None) -> List[Task]:
    return memory.list_tasks(status)


def create_task(data: TaskCreate) -> Task:
    return memory.create_task(data)


def get_task(task_id: int) -> Task:
    return memory.get_task(task_id)


def update_task(task_id: int, data: TaskUpdate) -> Task:
    return memory.update_task(task_id, data)


def delete_task(task_id: int) -> None:
    memory.delete_task(task_id)
