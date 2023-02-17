from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:hoge@localhost:5432/test_flask"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)

class Foods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    food_name = db.Column(db.String, nullable=False)

'''

create table users(
    id integer primary key,
    user_name varchar not null
);

create table foods(
    id integer primary key,
    user_id integer not null,
    food_name varchar not null,
    foreign key (user_id) references users(id)
    on delete cascade
    on update cascade
);


'''