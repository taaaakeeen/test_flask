from flask_restful import Resource
from flask import request
from account_manager import AccountManager

class Account(Resource):
    def __init__(self):
        self.getData = request.args.to_dict()

    def get(self):
        args = self.getData
        print(args)

    def post(self):
        try:
            args = self.getData

            if args["type"] == "add_user":
                user_id = request.json["user_id"]
                user_name = request.json["user_name"]
                password = request.json["password"]
                email = request.json["email"]
                manager = AccountManager()
                manager.add_user(user_id, user_name, password, email)

            elif args["type"] == "update_password":
                user_id = request.json["user_id"]
                password = request.json["password"]
                manager = AccountManager()
                manager.update_user(user_id, password=password)

        except Exception as e:
            print(e)
			# logging.exception("error details")
            return {'message':"5xx Server Error"}, 500

    def delete(self):
        args = self.getData
        print(args)

if __name__ == '__main__':
    pass

'''
http://127.0.0.1:3000/api/v1/account?type=hoge

{
    "user_id": "kenta1991",
    "user_name": "takahashi-kenta",
    "password": "hoge",
    "email": "kenta@gmail.com"
}


'''