from db.run_sql import run_sql
import repositories.employee_db as employee_sql
import repositories.project_db as project_sql
from models.employee_project import employee_sql, EmployeeProject


def add(employee_project):
    query = 'INSERT INTO employee_projects (employee_id, project_id) = (%s, %s) RETURNING id'
    values = [employee_project.employee.id, employee_project.project.id]
    results = run_sql(query, values)
    employee_project.id = results[0]['id']

def select_all():
    employee_projects = []
    query = 'SELECT * FROM employee_projects'
    results = run_sql(query)
    for row in results:
        project = project_sql.select(row['project_id'])
        employee = employee_sql.select(row['employee_id'])
        employee_project = EmployeeProject(project=project, employee=employee)
        employee_projects.append(employee_project)

    return employee_projects

def select(id):
    query = 'SELECT * FROM employee_projects WHERE id = %s'
    result = run_sql(query, [id])
    project = project_sql.select(result['project_id'])
    employee = employee_sql.select(result['employee_id'])
    employee_project = EmployeeProject(employee=employee, project=project)

    return employee_project

def delete(id):
    query = "DELETE FROM employee_projects WHERE id = %s"
    run_sql(query, id)

def update(employee_project):
    query = 'UPDATE employee_projects SET (employee_id, project_id) = (%s, %s) WHERE id = %s'
    values = [employee_project.employee.id, employee_project.project.id, employee_project.id]
    run_sql(query, values)

def delete_all():
    run_sql('DELETE FROM employee_projects')