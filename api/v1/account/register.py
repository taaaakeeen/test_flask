from flask_restful import Resource
from flask import request
from account_manager import AccountManager

class AccountRegister(Resource):
    def __init__(self):
        pass

    def post(self):
        try:
            print(request.json)
            user_id = request.json["user_id"]
            user_name = request.json["user_name"]
            password = request.json["password"]
            email = request.json["email"]
            
            AccountManager().add_user(user_id, user_name, password, email)
            res = {
                "status": "success",
                "message": "アカウントの作成に成功しました。"
            }
            return res, 200

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

http://127.0.0.1:3000/api/v1/account/register

{
    "user_id": "takaken1991",
    "user_name": "takahashi kenta",
    "password": "hogepiyo",
    "email": "kenta1991@gmail.com"
}

{
    "user_id": "hoge",
    "user_name": "hogeyama piyotaro",
    "password": "hogepiyo",
    "email": "hoge@gmail.com"
}

'''