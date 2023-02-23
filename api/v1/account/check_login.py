from flask_restful import Resource
from login_manager import LoginManager

class CheckLogin(Resource):
    def __init__(self):
        pass

    def get(self):
        return LoginManager().check_login()

if __name__ == '__main__':
    pass

'''
http://127.0.0.1:3000/api/v1/account/check_login


'''