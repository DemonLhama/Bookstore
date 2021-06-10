from flask_restful import reqparse, Resource
from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended import create_access_token,jwt_required,get_jwt
from werkzeug.security import safe_str_cmp
from bookstore.auth.usermodel import User
from blacklist import BLACKLIST


args = reqparse.RequestParser()
args.add_argument("email", type=str, help="This field cannot be left blank")
args.add_argument("username", type=str, required=True, help="This field cannot be left blank")
args.add_argument("password_hash", type=str, required=True)
args.add_argument("activated", type=bool)


class User_Actions(Resource):
    def get(self, username):
        user = User.find_user_username(username)
        if user:
            return user.json()
        return {"message": "User not found"}, 404

    @jwt_required()
    def delete(self, username):
        user = User.find_user_username(username)
        if user:
            try:
                user.delete_user()
            except:
                return {"message": "An error has ocurred when trying to delete the user"}, 500
            return {"message": "User deleted."}
        return {"message": "User not found"}, 404


class User_Register(Resource):
    def post(self):
        data = args.parse_args()

        if User.find_user_username(data["username"]):
            return {"message": "The username {} already exists.".format(data["username"])}

        user = User(**data)
        user.activated = False
        user.save_user()
        return {"message": "User succesfully created"}, 201 


class Login(Resource):
    @classmethod
    def post(cls):
        data = args.parse_args()
        user = User.find_user_username(data["username"])

        if user and safe_str_cmp(user.password_hash, data["password_hash"]):
            if user.activated:
                token = create_access_token(identity=user.user_id)
                return {"access_token": token}, 200
            return {"message": "User not confirmed"}, 400
        return {"message": "Username or password incorrect"}, 401

class ConfirmUser(Resource):
    @classmethod
    def get(cls, username):
        user = User.find_user_username(username)
        if not user:
            return {"message": "The username {} does not exists.".format(username)}
        user.activated = True
        user.save_user()
        return {"message": "Username {} has been confirmed".format(username)}

class Logout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()["jti"]
        BLACKLIST.add(jwt_id)
        return {"message": "Logged out successfully."}, 200