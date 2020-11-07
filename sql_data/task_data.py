from db.run_sql import run_sql
from models.task import Task

def add(task):
    query = 'INSERT INTO tasks (name, description, completed_amount, completed) VALUES (%s, %s, %s, %s) RETURNING id'
    result = run_sql(query, [task.name, task.description, task.completed_amount, task.completed])
    task.id = result[0]['id']

def select_all():
    tasks = []
    query = 'SELECT * FROM tasks'
    results = run_sql(query)
    for row in results:
        task = Task(name=row['name'], description=row['description'], id=row['id'],
                    completed_amount=row['completed_amount'], completed=row['completed'])
        tasks.append(task)

    return tasks

def select(task_id):
    query = 'SELECT * FROM tasks WHERE id = %s'
    rs = run_sql(query, [task_id])
    task = Task(name=rs['name'], description=rs['description'], id=rs['id'],
                completed_amount=rs['completed_amount'], completed=rs['completed'])
    return tas

def delete(task):
    run_sql('DELETE FROM tasks WHERE id = %s', [task.id])

def update(task):
    query = 'UPDATE tasks SET (name, description, completed_amount, completed)' \
            ' = %s, %s, %s, %s WHERE id = %s'
    run_sql(query, [task.name, task.description, task.completed_amount, task.completed, task.id])

def delete_all():
    run_sql('DELETE FROM tasks')