from flask_restful import Resource
from login_manager import LoginManager

class Logout(Resource):
    def __init__(self):
        pass

    def get(self):
        return LoginManager().logout()

if __name__ == '__main__':
    pass

'''
http://127.0.0.1:3000/api/v1/account/logout

'''