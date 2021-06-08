from flask import Flask

from bookstore import config
from bookstore import db
from bookstore import cli
from bookstore import api
from bookstore import site
from bookstore import auth
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    api.init_app(app)
    site.init_app(app)
    auth.init_app(app)
    bootstrap = Bootstrap(app)
    return app
