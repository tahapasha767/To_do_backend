# Mini Tasks API

Mini Tasks API is a lightweight backend service for managing tasks.  
It provides a simple REST API to create, update, list, and delete tasks, with support for task status, filtering, and pagination.

The project is built using **FastAPI** and is intended as a small, easy-to-understand backend service.

---

## Features

- Create tasks with a title and optional description
- Update existing tasks
- List tasks with optional status filtering
- Pagination support using `limit` and `offset`
- Soft deletion of tasks
- Task status management:
  - `todo`
  - `in_progress`
  - `done`
- Automatic timestamps (`created_at`, `updated_at`)

---

## Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **Pytest**
- In-memory data storage

---

## Project Structure

