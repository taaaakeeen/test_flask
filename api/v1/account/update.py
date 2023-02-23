from flask_restful import Resource
from flask import request
from account_manager import AccountManager

class AccountUpdate(Resource):
    def __init__(self):
        pass

    def post(self):
        try:
            print(request.json)
            user_id = request.json["user_id"]
            user_name = request.json["user_name"]
            password = request.json["password"]
            email = request.json["email"]

            flg = AccountManager().authenticate_user(user_id, password)
            if not flg:
                res = {
                    "status": "failed",
                    "message": "ユーザーIDまたはパスワードに誤りがあります。"
                }
                return res, 401

            AccountManager().update_user(user_id, password=password, email=email, user_name=user_name)
            res = {
                "status": "success",
                "message": "アカウント情報の変更に成功しました。"
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

http://127.0.0.1:3000/api/v1/account/update

{
    "user_id": "hoge",
    "user_name": null,
    "password": "hogepiyo",
    "email": "hogepiyo@gmail.com"
}

'''

