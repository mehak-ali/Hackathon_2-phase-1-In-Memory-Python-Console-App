# Research for Evolution of Todo - Phase I

## Decision: In-Memory Data Storage

**Decision**: A simple Python dictionary will be used to store the to-do list in memory. The dictionary will use an integer ID as the key and the task object as the value.

**Rationale**:
- The Phase I specification explicitly forbids file-based or database persistence.
- An in-memory dictionary is the simplest possible way to store data for the lifetime of the application run.
- It is a standard Python feature with no external dependencies.

**Alternatives Considered**:
- **List of objects**: A list of task objects was considered, but a dictionary provides faster lookups by ID, which is required for updating and deleting tasks.

## Decision: Sequential ID Generation

**Decision**: Task IDs will be generated using a simple auto-incrementing integer counter.

**Rationale**:
- This is the most straightforward way to ensure unique IDs for an in-memory data store.
- It is easy to implement and sufficient for the scope of Phase I.

**Alternatives Considered**:
- **UUIDs**: Universally Unique IDs were considered but deemed overly complex for a simple, single-user, in-memory application. Sequential integers are easier for a user to type in a CLI.
