from flask import Flask, session, request, make_response, jsonify
from datetime import timedelta
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "freedom"
# app.config['SESSION_TYPE'] = 'filesystem'
# app.config["SESSION_COOKIE_NAME"] = "session"
app.permanent_session_lifetime = timedelta(minutes=30)
cors = CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://127.0.0.1:3099"}})
# Session(app)

@app.route('/account/login', methods=["GET", "POST"])
def login():
    print("--------------------------")
    print("login")
    print(request.method)
    if request.method == "POST":
        session["user_id"] = request.json["user_id"]
        session['logged_in'] = True
        print(session)
        # data = {'key1': 'value1', 'key2': 'value2'}
        # response = make_response(jsonify(data))
        # response.headers['Access-Control-Expose-Headers'] = 'Authorization'
        # print(vars(response))
        print("--------------------------")
        res = "hoge"
        return res
    
    elif request.method == "GET":
        session["user_id"] = "takaken1991"
        session['logged_in'] = True
        print(session)
        return "hoge"

@app.route('/account/check_login', methods=["GET", "POST"])
def check_login():
    print("--------------------------")
    print("check_login")
    # print(request.headers)
    # print(request.method)
    print(session)
    flg = 'logged_in' in session
    print(flg)
    res = str(flg)
    return res

@app.route("/")
def hello_world():
    session["user_id"] = "hage"
    session['logged_in'] = True
    print(session)
    return "hoge"
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5098, debug=True, threaded=True)