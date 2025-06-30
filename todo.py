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
    cursor.execute("select id, description from tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("delete from tasks where id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
