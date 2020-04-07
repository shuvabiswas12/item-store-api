import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel as User


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="This field cannot be empty!"
    )

    parser.add_argument("password",
                        type=str,
                        required=True,
                        help='This field cannot be empty!'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"Message": "A user with that username already exits!"}, 400

        user = User(**data)
        user.save_to_db()

        return {'Message': "User created successfully"}, 201



