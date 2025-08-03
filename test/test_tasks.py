from datetime import datetime
import pytest
from src.controller.controller import tasks, create_task

@pytest.fixture
def setup_tasks():
    tasks.clear()

data1 = {
    "title": "Title 1",
    "description": "Description 1"
}

def test__create_task():
    task = create_task(**data1)
    assert task.title == data1["title"]
    assert isinstance(task.created_at, datetime)
    assert len(tasks) == 2

