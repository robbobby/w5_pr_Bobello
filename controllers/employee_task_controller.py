from flask import Blueprint, Flask, redirect, render_template, request
from models.employee_task import EmployeeTasks

import repositories.employee_tasks_db as emp_task_db

employee_tasks_blueprint = Blueprint('employee_tasks', __name__)

            ##### Employee Tasks Home Page #####

@employee_tasks_blueprint.route('/emp-tasks')
def emp_tasks():
    emp_tasks = emp_task_db.get_all()
    return render_template('employee_tasks/index.html', emp_tasks=emp_tasks)