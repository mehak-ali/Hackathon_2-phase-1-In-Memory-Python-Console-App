# Data Model for Evolution of Todo - Phase I

This document defines the data structures for the in-memory to-do list application.

## Task Entity

The core entity of the application is the `Task`.

**Attributes**:

| Attribute   | Type    | Description                                         | Constraints      |
|-------------|---------|-----------------------------------------------------|------------------|
| `id`        | integer | A unique identifier for the task.                   | Required, Unique |
| `description` | string  | The text content of the task.                       | Required, Not Empty |
| `completed` | boolean | The completion status of the task. Default is `false`. | Required         |

**Example**:

```python
{
    "id": 1,
    "description": "Buy milk",
    "completed": False
}
```

## In-Memory Store

The collection of tasks will be stored in a Python dictionary.

- **Structure**: `{ task_id: task_object }`
- **Example**:

```python
{
    1: {"id": 1, "description": "Buy milk", "completed": False},
    2: {"id": 2, "description": "Walk the dog", "completed": True}
}
```
