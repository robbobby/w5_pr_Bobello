from db.run_sql import run_sql
from models.employee import Employee

def add(employee):
    query = 'INSERT INTO employees (name) VALUES (%s) RETURNING *'
    values = employee.name
    results = run_sql(query, values)
    employee.id = results[0]['id']

def select_all():
    employees = []
    query = 'SELECT * FROM employees'
    results = run_sql(query)
    for row in results:
        employee = Employee(name=row['name'], id=row['id'])
        employees.append(employee)

    return employees

def select(employee_id):
    query = 'SELECT * FROM employees WHERE id = %s'
    rs = run_sql(query, [employee_id])
    employee = Employee(name=rs['name'], id=rs['id'])
    return employee

def delete(employee):
    run_sql('DELETE FROM employees WHERE id = %s', [employee.id]) ##### Bad practice? <--- No query or values

def update(employee)
    query = 'UPDATE employees SET name = %s WHERE id = %s'
    values = [employee.name, employee.id]
    run_sql(query, values)

def delete_all():
    run_sql('DELETE FROM employees')