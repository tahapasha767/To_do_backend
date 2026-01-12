from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class TaskCreate(BaseModel):
    title: constr(min_length=1)  # Add validation to ensure title is not empty
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    created_at: datetime
    updated_at: datetime
    deleted: bool = False