from flask_restful import Resource
from flask import request
from account_manager import AccountManager

class AccountDelete(Resource):
    def __init__(self):
        pass

    def delete(self):
        try:
            print(request.json)
            user_id = request.json["user_id"]
            password = request.json["password"]

            flg = AccountManager().authenticate_user(user_id, password)
            if not flg:
                res = {
                    "status": "failed",
                    "message": "ユーザーIDまたはパスワードに誤りがあります。"
                }
                return res, 401

            AccountManager().delete_user(user_id)
            res = {
                "status": "success",
                "message": "アカウントの削除に成功しました。"
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

http://127.0.0.1:3000/api/v1/account/delete

{
    "user_id": "hoge",
    "password": "hogepiy"
}

'''