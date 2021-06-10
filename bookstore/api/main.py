from flask_restful import Api
from flask import Blueprint
from bookstore.api.resources.category import Categories, Category
from bookstore.api.resources.books import Books, Book_Catalog, Book_Search
from bookstore.auth.user_auth import User_Actions,User_Register,ConfirmUser,Login,Logout

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(Categories, "/categories")
api.add_resource(Books, "/books")
api.add_resource(Book_Catalog, "/books/<int:book_id>")
api.add_resource(Category, "/categories/<string:category>")
api.add_resource(Book_Search, "/booksearch")
api.add_resource(User_Actions, "/users/<string:username>")
api.add_resource(User_Register, "/registrate")
api.add_resource(ConfirmUser, "/confirmation/<string:username>")
api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
