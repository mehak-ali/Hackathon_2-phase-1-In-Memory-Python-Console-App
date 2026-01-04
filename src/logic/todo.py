from src.data.store import task_store, Task
from typing import List

class TaskNotFoundError(Exception):
    pass

def add_task(description: str) -> Task:
    if not description or not description.strip():
        raise ValueError("Task description cannot be empty.")
    return task_store.add(description.strip())

def get_all_tasks() -> List[Task]:
    return list(task_store.get_all().values())

def update_task_description(task_id: int, new_description: str) -> Task:
    if not new_description or not new_description.strip():
        raise ValueError("Task description cannot be empty.")
    updated_task = task_store.update(task_id, new_description.strip())
    if updated_task is None:
        raise TaskNotFoundError(f"Task with ID {task_id} not found.")
    return updated_task

def set_task_status(task_id: int, completed: bool) -> Task:
    updated_task = task_store.set_status(task_id, completed)
    if updated_task is None:
        raise TaskNotFoundError(f"Task with ID {task_id} not found.")
    return updated_task

def delete_task(task_id: int):
    deleted_task = task_store.delete(task_id)
    if deleted_task is None:
        raise TaskNotFoundError(f"Task with ID {task_id} not found.")
