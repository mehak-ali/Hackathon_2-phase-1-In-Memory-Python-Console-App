import pytest
from src.logic.todo import add_task, get_all_tasks, update_task_description, set_task_status, delete_task, TaskNotFoundError
from src.data.store import task_store, Task

@pytest.fixture(autouse=True)
def setup_teardown():
    # Clear the task store before each test
    task_store._tasks = {}
    task_store._next_id = 1
    yield

def test_add_task_success():
    description = "Buy groceries"
    task = add_task(description)
    assert task is not None
    assert task['id'] == 1
    assert task['description'] == description
    assert task['completed'] is False

def test_add_task_empty_description():
    with pytest.raises(ValueError, match="Task description cannot be empty."):
        add_task("")

def test_add_task_whitespace_description():
    with pytest.raises(ValueError, match="Task description cannot be empty."):
        add_task("   ")

def test_get_all_tasks_empty():
    tasks = get_all_tasks()
    assert len(tasks) == 0

def test_get_all_tasks_with_tasks():
    add_task("Task 1")
    add_task("Task 2")
    tasks = get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0]['description'] == "Task 1"
    assert tasks[1]['description'] == "Task 2"

def test_update_task_description_success():
    task = add_task("Old description")
    updated_task = update_task_description(task['id'], "New description")
    assert updated_task['description'] == "New description"
    assert task_store.get_by_id(task['id'])['description'] == "New description"

def test_update_task_description_not_found():
    with pytest.raises(TaskNotFoundError, match="Task with ID 999 not found."):
        update_task_description(999, "Some description")

def test_update_task_description_empty_new_description():
    task = add_task("Existing task")
    with pytest.raises(ValueError, match="Task description cannot be empty."):
        update_task_description(task['id'], "")

def test_update_task_description_whitespace_new_description():
    task = add_task("Existing task")
    with pytest.raises(ValueError, match="Task description cannot be empty."):
        update_task_description(task['id'], "   ")

def test_set_task_status_complete_success():
    task = add_task("Task to complete")
    completed_task = set_task_status(task['id'], True)
    assert completed_task['completed'] is True
    assert task_store.get_by_id(task['id'])['completed'] is True

def test_set_task_status_incomplete_success():
    task = add_task("Task to incomplete")
    completed_task = set_task_status(task['id'], True)
    incomplete_task = set_task_status(task['id'], False)
    assert incomplete_task['completed'] is False
    assert task_store.get_by_id(task['id'])['completed'] is False

def test_set_task_status_not_found():
    with pytest.raises(TaskNotFoundError, match="Task with ID 999 not found."):
        set_task_status(999, True)

def test_delete_task_success():
    task = add_task("Task to delete")
    delete_task(task['id'])
    assert task_store.get_by_id(task['id']) is None
    assert len(get_all_tasks()) == 0

def test_delete_task_not_found():
    add_task("Existing task")
    with pytest.raises(TaskNotFoundError, match="Task with ID 999 not found."):
        delete_task(999)