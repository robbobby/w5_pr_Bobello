from db.run_sql import run_sql
import repositories.employee_db as employee_sql
import repositories.task_db as task_sql
from models.employee_task import employee_sql, Employeetask


def add(employee_task):
    query = 'INSERT INTO employee_tasks (employee_id, task_id) = (%s, %s) RETURNING id'
    values = [employee_task.employee.id, employee_task.task.id]
    results = run_sql(query, values)
    employee_task.id = results[0]['id']

def select_all():
    employee_tasks = []
    query = 'SELECT * FROM employee_tasks'
    results = run_sql(query)
    for row in results:
        task = task_sql.select(row['task_id'])
        employee = employee_sql.select(row['employee_id'])
        employee_task = Employeetask(task=task, employee=employee)
        employee_tasks.append(employee_task)

    return employee_tasks

def select(id):
    query = 'SELECT * FROM employee_tasks WHERE id = %s'
    result = run_sql(query, [id])
    task = task_sql.select(result['task_id'])
    employee = employee_sql.select(result['employee_id'])
    employee_task = Employeetask(employee=employee, task=task)

    return employee_task

def delete(id):
    query = "DELETE FROM employee_tasks WHERE id = %s"
    run_sql(query, id)

def update(employee_task):
    query = 'UPDATE employee_tasks SET (employee_id, task_id) = (%s, %s) WHERE id = %s'
    values = [employee_task.employee.id, employee_task.task.id, employee_task.id]
    run_sql(query, values)

def delete_all():
    run_sql('DELETE FROM employee_tasks')