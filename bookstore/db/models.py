from bookstore.db import db

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column("id", db.Integer, primary_key=True)
    category = db.Column("category", db.String, unique=True)
    books = db.relationship('Book', backref='category')

    def __repr__(self):
        return '<Category %r>' % self.category



class Book(db.Model):
    __tablename__ = "books"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.Unicode, index=True)
    author = db.Column("author", db.Unicode, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return '<Book %r>' % self.title
