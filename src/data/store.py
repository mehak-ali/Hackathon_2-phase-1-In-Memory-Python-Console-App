from typing import TypedDict, Dict

class Task(TypedDict):
    id: int
    description: str
    completed: bool

class TaskStore:
    _tasks: Dict[int, Task]
    _next_id: int

    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def get_all(self) -> Dict[int, Task]:
        return self._tasks

    def get_by_id(self, task_id: int) -> Task | None:
        return self._tasks.get(task_id)

    def add(self, description: str) -> Task:
        task = Task(id=self._next_id, description=description, completed=False)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def update(self, task_id: int, description: str) -> Task | None:
        if task_id in self._tasks:
            self._tasks[task_id]['description'] = description
            return self._tasks[task_id]
        return None

    def set_status(self, task_id: int, completed: bool) -> Task | None:
        if task_id in self._tasks:
            self._tasks[task_id]['completed'] = completed
            return self._tasks[task_id]
        return None

    def delete(self, task_id: int) -> Task | None:
        return self._tasks.pop(task_id, None)

task_store = TaskStore()
