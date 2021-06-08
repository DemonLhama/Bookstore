from flask_restful import Resource, reqparse
from bookstore.db.models import CategoryTable

args = reqparse.RequestParser()
args.add_argument("category", type=str, required=True)

class Categories(Resource):
    def get(self):
        return {"categories": [categories.json() for categories in CategoryTable.query.all()]}


    def post(self):
        data = args.parse_args()
        if CategoryTable.find_category(data['category']):
            return {"message": "The {} category already exists.".format(data['category'])}, 400

        category = CategoryTable(**data)

        category.create_category()
        return {"message": "Category sucessfully created."}, 201

class Category(Resource):
    def delete(self, category):
        catg = CategoryTable.find_category(category)
        if catg:
            try:
                catg.delete_catg()
            except:
                return {"message": "An internal error has ocurred."}
            return {"message": "The category has been deleted."}
        return {"message": "Category not found."}



    def put(self, category):
        data = args.parse_args()
        catg_search = CategoryTable.find_category(category)

        if catg_search:
            catg_search.update_category(**data)
            catg_search.create_category()
            return catg_search.json(), 200

        catg = CategoryTable(**data)

        try:
            catg.create_category()
        except:
            return {"message": "An internal error has ocurred"}, 500

        return catg.json(), 201



