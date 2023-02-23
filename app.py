from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.v1.test import Test
from api.v1.account.register import AccountRegister
from api.v1.account.update import AccountUpdate
from api.v1.account.delete import AccountDelete
from api.v1.account.login import Login
from api.v1.account.logout import Logout
from api.v1.account.check_login import CheckLogin
import database.test_flask_database as DB
from dotenv import load_dotenv
import os
from datetime import timedelta 

load_dotenv()
TEST_FLASK_DATABASE =  os.environ['TEST_FLASK_DATABASE_URL']

class App():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.cors = CORS(self.app, resources={r"/*": {"origins": "*"}})
        self.app.secret_key = "password" # os.urandom(24)
        self.app.permanent_session_lifetime = timedelta(minutes=3) 
        self.app.config["SQLALCHEMY_DATABASE_URI"] = TEST_FLASK_DATABASE
        self.app.config["SQLALCHEMY_ECHO"] = False
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        DB.db.init_app(self.app)

    def init_api(self):
        self.api.add_resource(Test, "/api/v1/test")
        self.api.add_resource(AccountRegister, "/api/v1/account/register")
        self.api.add_resource(AccountUpdate, "/api/v1/account/update")
        self.api.add_resource(AccountDelete, "/api/v1/account/delete")
        self.api.add_resource(Login, "/api/v1/account/login")
        self.api.add_resource(Logout, "/api/v1/account/logout")
        self.api.add_resource(CheckLogin, "/api/v1/account/check_login")

    def post(self):
        pass

    def delete(self):
        pass

class Server(App):
    def __init__(self):
        super().__init__()
        self.init_api()

if __name__ == '__main__':
    server = Server()
    server.app.run(host="0.0.0.0", port=3000, debug=True, threaded=True)