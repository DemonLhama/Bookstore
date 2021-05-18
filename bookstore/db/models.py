from bookstore.db import db



class Book(db.Model):
    __tablename__ = "books"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.Unicode, index=True)
    author = db.Column("author", db.Unicode, index=True)
    category = db.Column("category", db.Unicode, index=True)
