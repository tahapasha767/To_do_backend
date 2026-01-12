# Mini Tasks API

Mini Tasks API is a lightweight backend service for managing tasks.
It provides a REST API to create, update, list, and delete tasks with basic
status tracking and pagination support.

## Features

- Create tasks with title and description
- Update task details and status
- List tasks with optional status filtering
- Pagination using limit and offset
- Soft deletion of tasks
- Automatic timestamps

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pytest
- In-memory storage

## Running Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload



---

## File and Module Overview

### `app.py`
The main entry point of the application.

- Creates the FastAPI application instance
- Loads application configuration
- Registers API routers

This file is intentionally small and focused on bootstrapping the app.

---

### `api/`
Contains all HTTP route definitions.

#### `api/tasks.py`
Defines the REST API endpoints related to task management.

Responsibilities:
- Parse and validate HTTP requests
- Handle query parameters (filtering, pagination)
- Convert domain errors into HTTP responses
- Delegate business logic to the service layer

This layer should not contain business logic.

---

### `core/`
Contains application-wide configuration and setup.

#### `core/config.py`
Holds application settings such as:
- Application name
- Debug flags

Configuration is loaded using environment variables when available.

---

### `models/`
Defines the data models and request/response schemas.

#### `models/task.py`
Contains:
- Task status enum
- Request schemas for creating and updating tasks
- Response model for task objects

These models define the shape of data exchanged through the API.

---

### `services/`
Contains the business logic of the application.

#### `services/task_service.py`
Implements task-related operations such as:
- Creating tasks
- Updating tasks
- Listing tasks
- Deleting tasks

This layer acts as the boundary between the API layer and the storage layer.

---

### `storage/`
Responsible for data persistence.

#### `storage/memory.py`
Implements an in-memory data store for tasks.

Responsibilities:
- Store task records
- Handle basic CRUD operations
- Manage soft deletion

This module can later be replaced with a database-backed implementation.

---

### `tests/`
Contains automated tests for the application.

#### `tests/test_tasks.py`
Includes basic tests for:
- Task creation
- Task listing

Tests are written using Pytest and FastAPI’s test client.

---

### `requirements.txt`
Lists the Python dependencies required to run the application.

---

## Notes on Architecture

- The project follows a layered architecture:
  - **API layer** handles HTTP concerns
  - **Service layer** contains business logic
  - **Storage layer** handles persistence
- Each layer has a single responsibility
- The design makes it easy to extend or replace components

---

This structure is intentionally simple but follows patterns commonly used
in production FastAPI applications.
