import os.path
from bookstore.api.resources.filters import *
import sqlite3
from flask_restful import Resource, reqparse
from bookstore.db.models import BookTable, CategoryTable

args = reqparse.RequestParser()
args.add_argument("title", type=str, required=True)
args.add_argument("author", type=str, required=True)
args.add_argument("category", type=str, required=True)

class Books(Resource):

    def post(self):
        data = args.parse_args()

        if BookTable.find_book_title(data.get("title")):
            return {"message": "This book already exists.".format(data.get("author"))}, 400
        book = BookTable(**data)

        if not CategoryTable.find_category(data.get('category')):
            return {"message": "The book must be associated to a valid category"}, 400
        
        try:
            book.save_book()
        except:
            return {"message": "An internal error has ocurred."}, 500

        return book.json()


class Book_Catalog(Resource):

    def get(self, book_id):
        book = BookTable.find_book_id(book_id)
        if book:
            return book.json()
        return {"message": "Book not found"}, 404


    def put(self, book_id):
        data = args.parse_args()
        book_search = BookTable.find_book_id(book_id)

        if book_search:
            book_search.book_update(**data)
            book_search.save_book()
            return book_search.json(), 200

        book = BookTable(**data)

        try:
            book.save_book()
        except:
            return {"message": "An internal error has ocurred"}, 500

        return book.json(), 201


    def delete(self, book_id):
        book = BookTable.find_book_id(book_id)
        if book:
            try:
                book.delete_book()
            except:
                return {"message": "An error has ocurred when trying to delete this book"}, 500
            return {"message": "Book deleted"}
        return {"message": "Book not found"}, 404



search_params = reqparse.RequestParser()
search_params.add_argument("title", type=str)
search_params.add_argument("author", type=str)
search_params.add_argument("category", type=str)
search_params.add_argument("limit", type=float)
search_params.add_argument("offset", type=float)

class Book_Search(Resource):

    def get(self):

        connection = sqlite3.connect("bookstore/bookstore.db")
        cursor = connection.cursor()
        data = search_params.parse_args()
        valid_data = {key:data[key] for key in data if data[key] is not None}
        params = search_normalize(**valid_data)

        
        if not params.get("category") and not params.get("title"):
            tupla = tuple([params[keys] for keys in params])
            results = cursor.execute(author_consult, tupla)

        if not params.get("author") and not params.get("title"):
            tupla = tuple([params[keys] for keys in params])
            results = cursor.execute(catg_consult, tupla)

        if not params.get("author") and not params.get("category"):
            tupla = tuple([params[keys] for keys in params])
            results = cursor.execute(title_consult, tupla)

        books = []
        for line in results:
            books.append({
                "book_id": line[0],
                "title": line[1],
                "author": line[2],
                "category": line[3]
            })

        return {"books": books}
