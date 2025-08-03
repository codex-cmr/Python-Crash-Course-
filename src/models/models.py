from datetime import datetime
from enum import Enum
from pydantic import BaseModel

tasks = []

class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"

class Task(BaseModel):
    id : str
    title : str
    description: str
    created_at: datetime
    status: TaskStatus


