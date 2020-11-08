from flask import Blueprint, Flask, redirect, render_template, request

from models.company import Company
import repositories.company_db as company_db

companies_blueprint = Blueprint("companies", __name__)


                ##### Companies Home Page #####
@companies_blueprint.route("/companies")
def companies():
    companies = company_db.get_all()
    return render_template("companies/index.html", companies=companies)
