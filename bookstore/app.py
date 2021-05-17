from flask import Flask

from bookstore import config
from bookstore import db
from bookstore import cli


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    return app
