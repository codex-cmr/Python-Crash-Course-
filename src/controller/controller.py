from datetime import datetime
from typing import List
from uuid import uuid4
from src.models.models import Task, TaskStatus

tasks = []

def create_task(title:str, description:str) -> Task:
        task = Task(
            id = str(uuid4()),
            title = title,
            description = description,
            created_at = datetime.utcnow(),
            status= TaskStatus.PENDING
        )
        tasks.append(task)
        return  task


def get_tasks() -> List[Task]:
    return tasks