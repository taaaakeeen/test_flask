from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.v1.test import Test
from api.v1.account import Account
import database.test_flask_database as DB
from dotenv import load_dotenv
import os

load_dotenv()
TEST_FLASK_DATABASE =  os.environ['TEST_FLASK_DATABASE_URL']

class App():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.cors = CORS(self.app, resources={r"/*": {"origins": "*"}})
        self.app.config["SQLALCHEMY_DATABASE_URI"] = TEST_FLASK_DATABASE
        self.app.config["SQLALCHEMY_ECHO"] = False
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        DB.db.init_app(self.app)

    def init_api(self):
        self.api.add_resource(Test, "/api/v1/test")
        self.api.add_resource(Account, "/api/v1/account")

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