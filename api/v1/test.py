from flask_restful import Resource
import database.test_flask_database as DB
from database.test_flask_database import Users, Foods
from flask import request
from login_manager import LoginManager

class Test(Resource):
    def __init__(self):
        self.getData = request.args.to_dict()

    def get(self):

        # 防御魔法
        ##########################################################
        result = LoginManager().protego()
        if result["defense"]:
            return result["response"], result["status_code"]
        ##########################################################

        args = self.getData
        print(args)

        if args["type"] == "1":

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

'''

http://127.0.0.1:3000/api/v1/test?type=1


'''