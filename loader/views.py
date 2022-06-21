from flask import Flask, Blueprint, render_template


# 4: Create Blueprint loader_blueprint:
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


# 4: Create decorator by '/post' for create new post:
@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')
