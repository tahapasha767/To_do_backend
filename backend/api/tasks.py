from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models.task import Task, TaskCreate, TaskUpdate, TaskStatus
from services import task_service

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=List[Task])
def list_tasks(
    status: Optional[TaskStatus] = Query(None),
    limit: int = 100,
    offset: int = 0,
):
    tasks = task_service.list_tasks(status)
    return tasks[offset : offset + limit]


@router.post("/", response_model=Task)
def create_task(task: TaskCreate):
    return task_service.create_task(task)


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    try:
        return task_service.get_task(task_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Task not found")


@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, data: TaskUpdate):
    try:
        return task_service.update_task(task_id, data)
    except KeyError:
        raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}")
def delete_task(task_id: int):
    try:
        task_service.delete_task(task_id)
        return {"status": "deleted"}
    except KeyError:
        raise HTTPException(status_code=404, detail="Task not found")
