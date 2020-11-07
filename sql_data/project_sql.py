from db.run_sql import run_sql
from models.project import Project

def add(project):
    query = 'INSERT INTO projects (name, company_id) VALUES (%s, %s) RETURNING id'
    result = run_sql(query, [project.name, project.company_id])
    project.id = result[0]['id']

def select_all():
    projects = []
    query = 'SELECT * FROM projects'
    results = run_sql(query)
    for row in results:
        project = Project(name=row['name'], id=row['id'], company_id=row['company_id'])
        projects.append(project)

    return projects

def select(project_id):
    query = 'SELECT * FROM projects WHERE id = %s'
    rs = run_sql(query, [project_id])
    project = Project(name=rs['name'], id=rs['id'], company_id=rs['company_id'])
    return project

def delete(project):
    run_sql('DELETE FROM projects WHERE id = %s', [project.id])

def update(project):
    query = 'UPDATE projects SET (name, company_id) = (%s, %s) WHERE id = %s'
    run_sql(query, [project.name, project.company_id, project.id])

def delete_all():
    run_sql('DELETE FROM projects')