from flask_restful import Resource, reqparse
from bookstore.db.models import Category



class Categories(Resource):
    def post(self):
        args = reqparse.RequestParser()
        args.add_argument("category", type=str, required=True)
        data = args.parse_args()
        if Category.find_category(data['category']):
            return {"message": "The {} category already exists.".format(data['category'])}, 400

        category = Category(**data)

        category.create_category()
        return {"message": "Category sucessfully created."}, 201


