from bookstore.db import db


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, unique=True, index=True)
    books = db.relationship('Book', backref='category')


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.Integer, index=True)
    author = db.Column("author", db.Unicode, index=True)
    category_id = db.Column("category_id", db.Integer, db.ForeignKey('categories.id'))
