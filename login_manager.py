from account_manager import AccountManager
from flask import session

class LoginManager():
    def __init__(self):
        pass

    def login(self, user_id, password):
        manager = AccountManager()
        flg = manager.authenticate_user(user_id, password)

        if not flg:
            res = {
                "status": "failed",
                "message": "ユーザーIDまたはパスワードに誤りがあります。"
            }
            return res, 401

        manager = AccountManager()
        user = manager.get_user(user_id)

        session["user_id"] = user.user_id
        session["user_name"] = user.user_name
        session['logged_in'] = True
        print(session)
        
        res = {
            "status": "success",
            "message": "ログインに成功しました。"
        }
        return res, 200

    def logout(self):
        session.pop('logged_in', None)
        print(session)
        return True

    def check_login(self):
        print(session)
        return 'logged_in' in session

    def protego(self):
        print(session)
        if not 'logged_in' in session:
            res = {
                "status": "failed",
                "message": "アクセス権限がありません"
            }
            return {"defense": True, "response":res, "status_code": 401}
        else:
            return {"defense": False}

if __name__ == '__main__':
    pass

        




