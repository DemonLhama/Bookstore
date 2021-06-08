from flask_restful import Api
from flask import Blueprint
from bookstore.api.resources.category import Categories
from bookstore.api.resources.books import Books, Book_Catalog

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(Categories, '/categories')
api.add_resource(Books, "/books")
api.add_resource(Book_Catalog, "/books/<int:book_id>")