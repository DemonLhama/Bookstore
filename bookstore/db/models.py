from sqlalchemy.orm import relationship
from flask_login import UserMixin
from bookstore.db import db
from bookstore.auth import login_manager



class CategoryTable(db.Model):
    __tablename__ = "categories"
    category_id = db.Column("category_id", db.Integer, primary_key=True)
    category = db.Column("category", db.Unicode, unique=True)
    books = db.relationship("BookTable", back_populates="category_books")

    def __repr__(self, category_id, category):
        self.category_id = category_id
        self.category = category

    def json(self):
        return {
            "category_id": self.category_id,
            "category": self.category,
        }

    def create_category(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def find_category(cls, category):
        category = cls.query.filter_by(category=category).first()
        if category:
            return category
        return None

    def update_category(self, category):
        self.category = category

    def delete_catg(self):
        db.session.delete(self)
        db.session.commit()



class BookTable(db.Model):
    __tablename__ = "books"
    book_id = db.Column("book_id", db.Integer, primary_key=True)
    title = db.Column("title", db.Unicode, index=True)
    author = db.Column("author", db.Unicode, index=True)
    category = db.Column(db.Unicode, db.ForeignKey('categories.category'))
    category_books = relationship("CategoryTable", back_populates="books")
    
    def __repr__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category

    def json(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            }

    @classmethod
    def find_book_title(cls, title):
        book = cls.query.filter_by(title=title).first()
        if book:
            return book
        return None

    @classmethod
    def find_book_id(cls, book_id):
        book = cls.query.filter_by(book_id=book_id).first()
        if book:
            return book
        return None

    def save_book(self):
        db.session.add(self)
        db.session.commit()

    def update_book(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category

    def delete_book(self):
        db.session.delete(self)
        db.session.commit()

    def book_update(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
