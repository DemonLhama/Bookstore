from sqlalchemy.orm import relationship
from flask_login import UserMixin
from bookstore.db import db



class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column("id", db.Integer, primary_key=True)
    category = db.Column("category", db.Unicode, unique=True)
    books = db.relationship("Book", back_populates="category_books")

    def __repr__(self):
        return self.category



class Book(db.Model):
    __tablename__ = "books"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.Unicode, index=True)
    author = db.Column("author", db.Unicode, index=True)
    category = db.Column(db.Unicode, db.ForeignKey('categories.category'))
    category_books = relationship("Category", back_populates="books")

    def __repr__(self):
        return self.title

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))