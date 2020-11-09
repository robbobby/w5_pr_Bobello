from db.run_sql import run_sql
from models.employee import Employee

def save(employee):
    query = 'INSERT INTO employees (name, company_id) VALUES (%s, %s) RETURNING *'
    values = [employee.name, employee.company.id]
    results = run_sql(query, values)
    employee.id = results[0]['id']

def get_all():
    employees = []
    query = 'SELECT * FROM employees'
    results = run_sql(query)
    for row in results:
        employee = Employee(name=row['name'], id=row['id'], company=rs['company_id'])
        employees.append(employee)

    return employees

def select(employee_id):
    query = 'SELECT * FROM employees WHERE id = %s'
    rs = run_sql(query, [employee_id])
    employee = Employee(name=rs['name'], id=rs['id'], company=rs['company_id'])
    return employee

def delete(employee):
    run_sql('DELETE FROM employees WHERE id = %s', [employee.id]) ##### Bad practice? <--- No query or values

def update(employee):
    query = 'UPDATE employees SET (name, company_id) = (%s, %s) WHERE id = %s'
    values = [employee.name, employee.company_id, employee.id]
    run_sql(query, values)

def delete_all():
    run_sql('DELETE FROM employees')