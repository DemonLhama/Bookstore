from bookstore.db import db
from bookstore.db.models import *

def init_app(app):

    @app.cli.command()
    def create_db():
        "Initialize the database"
        db.create_all()