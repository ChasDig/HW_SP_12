from flask import Flask, Blueprint, render_template, request
from functions import add_post
from loader.utils import picture_save

# 4: Create Blueprint loader_blueprint:
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


# 4: Create decorator by '/post' for create new post:
@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')


# 5: Create decorator '/post/(POST). Create a new post:
@loader_blueprint.route('/post/', methods=['POST'])
def add_post_page():

    picture = request.files.get('picture')
    content = request.form.get('content')

    save_pic = '/' + picture_save(picture)

    post: dict = add_post({'pic': save_pic, 'content': content})

    return render_template('post_uploaded.html', post=post[-1])
