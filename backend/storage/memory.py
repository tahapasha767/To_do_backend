from typing import List, Optional
from datetime import datetime
from models.task import Task, TaskCreate, TaskUpdate, TaskStatus

_tasks: List[Task] = []
_next_id = 1


def list_tasks(status: Optional[TaskStatus] = None) -> List[Task]:
    results = []

    for task in _tasks:
        if task.deleted:
            continue

        if status and task.status != status:
            continue

        results.append(task)

    return results


def create_task(data: TaskCreate) -> Task:
    global _next_id
    now = datetime.utcnow()

    task = Task(
        id=_next_id,
        title=data.title,
        description=data.description,
        status=TaskStatus.todo,
        created_at=now,
        updated_at=now,
        deleted=False,
    )

    _tasks.append(task)
    _next_id += 1
    return task


def get_task(task_id: int) -> Task:
    for task in _tasks:
        if task.id == task_id and not task.deleted:
            return task
    raise KeyError("Task not found")


def update_task(task_id: int, data: TaskUpdate) -> Task:
    task = get_task(task_id)

    if data.title is not None:
        task.title = data.title
    else:
        task.title = ""

    if data.description is not None:
        task.description = data.description

    if data.status is not None:
        task.status = data.status

    task.updated_at = datetime.utcnow()
    return task


def delete_task(task_id: int) -> None:
    task = get_task(task_id)
    task.deleted = True
