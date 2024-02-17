from flask import Blueprint, render_template , request

calculator_blueprint = Blueprint('calculator', __name__)

@calculator_blueprint.route('/calculator')
def calculator():
    return render_template("calculator.html")

@calculator_blueprint.route('/add', methods=['POST'])
def add():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 + num2
    return render_template('result.html', result=result)