from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_restful import Resource
from flask import request
import test_flask_database as DB
from test_flask_database import Users, Foods

class App():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.cors = CORS(self.app, resources={r"/*": {"origins": "*"}})
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:hoge@localhost:5432/test_flask"
        # self.app.config["SQLALCHEMY_ECHO"] = True
        DB.db.init_app(self.app)

    def init_api(self):
        self.api.add_resource(Test, "/test")

class Test(Resource):
    def __init__(self):
        self.getData = request.args.to_dict()

    def get(self):
        args = self.getData
        print(args)

        print("select * from users")
        rows = DB.Users.query.all()
        for row in rows:
            print(row.id, row.user_name)

        print("select * from foods")
        rows = DB.Foods.query.all()
        for row in rows:
            print(row.user_id, row.food_name)

        print("select * from foods")  
        rows = DB.db.session.query(DB.Foods).all()
        for row in rows:
            print(row.user_id, row.food_name)

        print("select * from foods where food_name = 'パスタ'")  
        rows = DB.db.session.query(DB.Foods).filter(DB.Foods.food_name == "パスタ")
        for row in rows:
            print(row.user_id, row.food_name)

        print("select * from users inner join foods on users.id = foods.user_id")
        rows = DB.db.session.query(DB.Users, DB.Foods).join(DB.Users, DB.Users.id == DB.Foods.user_id)
        for row in rows:
            print(row[0].id, row[0].user_name, row[1].food_name)

        print("select * from users inner join foods on users.id = foods.user_id where users.id = 1")
        rows = DB.db.session.query(Users, Foods).join(Users, Users.id == Foods.user_id).filter(Users.id == 1).all()
        for row in rows:
            print(row[0].id, row[0].user_name, row[1].food_name)

        return "hoge" 

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