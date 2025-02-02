from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from cc_simple_server.models import TaskCreate
from cc_simple_server.models import TaskRead
from cc_simple_server.database import init_db
from cc_simple_server.database import get_db_connection

app = FastAPI()

init_db()


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Cloud Computing!"}


@app.post("/tasks/", response_model=TaskRead)
async def create_task(task_data: TaskCreate):
    """Create a new task."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
        (task_data.title, task_data.description, task_data.completed),
    )
    conn.commit()
    id = cursor.lastrowid
    conn.close()

    return TaskRead(id=id, title=task_data.title, description=task_data.description, completed=task_data.completed)


@app.get("/tasks/", response_model=list[TaskRead])
async def get_tasks():
    """Retrieve all tasks."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, description, completed FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        return []

    return [TaskRead(id=row[0], title=row[1], description=row[2], completed=bool(row[3])) for row in tasks]


@app.put("/tasks/{task_id}/", response_model=TaskRead)
async def update_task(task_id: int, task_data: TaskCreate):
    """Update a task by its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?",
        (task_data.title, task_data.description, task_data.completed, task_id),
    )
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")

    conn.close()
    return TaskRead(id=task_id, **task_data.dict())


@app.delete("/tasks/{task_id}/")
async def delete_task(task_id: int):
    """Delete a task by its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")

    conn.close()
    return {"message": f"Task {task_id} deleted successfully"}
