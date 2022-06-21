from flask import Flask, request, render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# 2: Register Blueprint main_blueprint:
app.register_blueprint(main_blueprint)

# 4: Register Blueprint loader_blueprint:
app.register_blueprint(loader_blueprint)

# 6-7: Error handler: create logging:
logging.basicConfig(filename='basic.log', level=logging.INFO)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

