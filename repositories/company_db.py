from db.run_sql import run_sql
from models.company import Company

def add(company):
    query = 'INSERT INTO companies (name) VALUES (%s) RETURNING *;'
    values = company.name
    results = run_sql(query, values)
    company.id = results[0]['id']

def get_all():
    companies = []
    query = 'SELECT * FROM companies'
    results = run_sql(query)
    for company in results:
        company_to_add = Company(company['name'], company['id'])
        companies.append(company_to_add)

    return companies

def select(company_id):
    query = "Select * FROM companies WHERE id = %s"
    results = run_sql(query, [company_id])
    company = Company(results['name'], results['id'])
    return company


def delete(company):
    query = 'DELETE FROM companies WHERE id = %s'
    values = [company.id]
    run_sql(query, values)

def update(company):
    query = 'UPDATE companies SET name = %s WHERE id = %s'
    values = [company.name, company.id]
    run_sql(query, values)

def delete_all():
    run_sql('DELETE FROM companies')
