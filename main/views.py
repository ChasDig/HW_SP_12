from flask import Flask, Blueprint, render_template

# 2: Create Blueprint main_blueprint:
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# 2: Create decorate '/':
@main_blueprint.route('/')
def add_page_main():
    return render_template('index.html')
