from bookstore.db.models import Book
from bookstore.db import db


def add_book(title:str, author:str, category:int) -> Book:
    book = Book(
        title = title,
        author = author,
        category = category,
    )
    db.session.add(book)
    db.session.commit()
    return book

