from re import search
from bookstore.db.models import BookTable
from bookstore.db import db


def add_book(title:str, author:str, category:int) -> BookTable:
    book = BookTable(
        title = title,
        author = author,
        category = category,
    )
    db.session.add(book)
    db.session.commit()
    return book
