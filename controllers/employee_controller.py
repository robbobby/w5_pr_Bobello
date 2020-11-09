from flask import Blueprint, Flask, redirect, render_template, request

from models.employee import Employee
import repositories.employee_db as employee_db

employee_blueprint = Blueprint("employees", __name__)


            ##### Employees Home Page #####

@employee_blueprint.route("/employeee")
def employees():
    employees = employee_db.get_all()
    return render_template("companies/index.html", employees=employees)