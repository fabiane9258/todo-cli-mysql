from database import get_connection

def add_task(description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (%s)", (description,))
    conn.commit()
    cursor.close()
    conn.close()

def list_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    # Fetch completed status as well
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()

def toggle_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    # Get current status
    cursor.execute("SELECT completed FROM tasks WHERE id = %s", (task_id,))
    current_status = cursor.fetchone()[0]
    # Flip the status
    cursor.execute("UPDATE tasks SET completed = %s WHERE id = %s", (not current_status, task_id))
    conn.commit()
    cursor.close()
    conn.close()

def calculate_progress():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tasks")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE completed = TRUE")
    completed = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return int((completed / total) * 100) if total > 0 else 0
