import logging
from json import JSONDecodeError
from flask import Flask, Blueprint, render_template, request
from functions import search_page


# 2: Create Blueprint main_blueprint:
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# 2: Create decorate '/':
@main_blueprint.route('/')
def add_page_main():
    return render_template('index.html')


# 3: Create search by meaning:
@main_blueprint.route('/search')
def main_search_page():

    search_meaning = request.args['s']
    logging.info("Выполняется поиск!")

    # 6-7: Error handler:
    try:
        result_search_page = search_page(search_meaning)
    except FileNotFoundError:
        return "Файл не найден!"
    except JSONDecodeError:
        return "Невалидный файл"

    return render_template('post_list.html', posts=result_search_page, meaning=search_meaning)
