# Tasks: Evolution of Todo - Phase I

**Input**: Design documents from `specs/001-todo-phase-one/`
**Prerequisites**: plan.md, spec.md, data-model.md, research.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure: `src/`, `tests/` and subdirectories `src/data`, `src/logic`, `src/cli`, `tests/unit` as defined in `plan.md`.
- [X] T002 Create empty Python files: `src/__init__.py`, `src/data/__init__.py`, `src/data/store.py`, `src/logic/__init__.py`, `src/logic/todo.py`, `src/cli/__init__.py`, `src/cli/main.py`, `tests/__init__.py`, `tests/unit/__init__.py`, `tests/unit/test_todo.py`, `tests/unit/test_store.py`.

---

## Phase 2: Foundational (Data Model and Storage)

**Purpose**: Implement the core data structures for the application.

- [X] T003 In `src/data/store.py`, define the `Task` data class or TypedDict according to `data-model.md`. It should have `id` (int), `description` (str), and `completed` (bool) fields.
- [X] T004 In `src/data/store.py`, implement the in-memory store. This will include a dictionary to hold tasks and a counter for generating sequential task IDs.

---

## Phase 3: User Story 1 - Add Task

**Goal**: Allow a user to add a new task.
**Independent Test**: A user can call an "add" function, and a new task will appear in the data store.

- [X] T005 [US1] In `src/logic/todo.py`, implement the `add_task` function. It should accept a description, create a new `Task` object with a new unique ID, and save it to the in-memory store.
- [X] T006 [US1] In `tests/unit/test_todo.py`, write a unit test for the `add_task` function to verify a task is added correctly.

---

## Phase 4: User Story 2 - View Tasks

**Goal**: Allow a user to see all their tasks.
**Independent Test**: A user can call a "view" function and receive a list of all tasks in the store.

- [X] T007 [US2] In `src/logic/todo.py`, implement the `get_all_tasks` function that returns a list of all tasks from the store.
- [X] T008 [US2] In `tests/unit/test_todo.py`, write a unit test for `get_all_tasks` to verify it returns the correct list of tasks.

---

## Phase 5: User Story 3 - Update Task

**Goal**: Allow a user to edit a task's description.
**Independent Test**: A user can call an "update" function with an ID and new text, and the change will be reflected in the store.

- [X] T009 [US3] In `src/logic/todo.py`, implement the `update_task_description` function. It should take a task ID and a new description, find the task, and update its description. It should handle cases where the ID does not exist.
- [X] T010 [US3] In `tests/unit/test_todo.py`, write a unit test for `update_task_description`, including a test for a non-existent ID.

---

## Phase 6: User Story 4 - Mark Task Status

**Goal**: Allow a user to mark a task as complete or incomplete.
**Independent Test**: A user can call a "set status" function, and the task's `completed` flag will be updated in the store.

- [X] T011 [US4] In `src/logic/todo.py`, implement the `set_task_status` function. It should take a task ID and a boolean status and update the `completed` field of the corresponding task.
- [X] T012 [US4] In `tests/unit/test_todo.py`, write unit tests for `set_task_status` to verify it can mark a task both complete and incomplete.

---

## Phase 7: User Story 5 - Delete Task

**Goal**: Allow a user to remove a task.
**Independent Test**: A user can call a "delete" function with an ID, and the task will be removed from the store.

- [X] T013 [US5] In `src/logic/todo.py`, implement the `delete_task` function. It should take a task ID and remove the corresponding task from the store.
- [X] T014 [US5] In `tests/unit/test_todo.py`, write a unit test for `delete_task`, including a test for a non-existent ID.

---

## Phase 8: CLI and Finalization

**Purpose**: Create the user-facing command-line interface and tie all the logic together.

- [X] T015 In `src/cli/main.py`, implement the main application loop that displays the menu of options and reads the user's choice.
- [X] T016 In `src/cli/main.py`, integrate the `add_task` logic, prompting the user for a description.
- [X] T017 In `src/cli/main.py`, integrate the `get_all_tasks` logic and implement the display formatting for the list of tasks.
- [X] T018 In `src/cli/main.py`, integrate the `update_task_description` logic, prompting the user for the ID and new description.
- [X] T019 In `src/cli/main.py`, integrate the `set_task_status` logic, prompting the user for the ID and desired status.
- [X] T020 In `src/cli/main.py`, integrate the `delete_task` logic, prompting the user for the ID.
- [X] T021 In `src/cli/main.py`, implement robust error handling for invalid menu choices and invalid task IDs (e.g., "Task not found").
- [X] T022 In `src/cli/main.py`, implement the application entry point (`if __name__ == "__main__":`) to start the CLI loop.
