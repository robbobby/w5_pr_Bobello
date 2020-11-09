from flask import Blueprint, Flask, redirect, render_template, request

from models.company import Company
import repositories.company_db as company_db

companies_blueprint = Blueprint('companies', __name__)


                ##### Companies Home Page #####
@companies_blueprint.route('/companies', methods=['GET'])
def companies():
    companies = company_db.get_all()
    return render_template('companies/index.html', companies=companies)

@companies_blueprint.route('/companies/new', methods=['GET'])
def new_company():
    return render_template('companies/new.html')

@companies_blueprint.route('/companies', methods=['POST'])
def add_company():
    company = Company(request.form['name'])
    company_db.save(company)
    return redirect('/companies')
        ### How do we do this so when we have made a company is uses that id from that point on ###