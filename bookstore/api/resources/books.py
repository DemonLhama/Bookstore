from flask_restful import Resource, reqparse
from bookstore.db.models import BookTable, CategoryTable

args = reqparse.RequestParser()
args.add_argument("title", type=str, required=True)
args.add_argument("author", type=str, required=True)
args.add_argument("category", type=str, required=True)

class Books(Resource):
    def get_title(self, book_id):
        book = BookTable.find_book_id(book_id)
        if book:
            return book.json()
        return {"message": "Book not found"}, 404


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
