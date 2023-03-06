from flask import Flask
from config_app import Config
from flask_restx import Api
from config_db import db
from create_db import create_db
from view.frameworkmodel import framework_ns


def creating_app(config_app):
    app = Flask(__name__)
    app.config.from_object(config_app)
    app.app_context().push()
    register_ext(app)
    return app


def register_ext(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(framework_ns)
    create_db()


app = creating_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
