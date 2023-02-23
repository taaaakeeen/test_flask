from flask import request
from flask_restful import Resource
from login_manager import LoginManager

class Login(Resource):
    def __init__(self):
        pass

    def post(self):
        try:
            print(request.json)
            user_id = request.json["user_id"]
            password = request.json["password"]
            return LoginManager().login(user_id, password)

        except Exception as e:
            print(e)
			# logging.exception("error details")
            res = {
                "status": "failed",
                "message": "Internal Server Error"
            }
            return res, 500

if __name__ == '__main__':
    pass

'''
http://127.0.0.1:3000/api/v1/account/login

{
    "user_id": "takaken1991",
    "password": "hogepiyo"
}

{
    "user_id": "wataru",
    "password": "password"
}

'''