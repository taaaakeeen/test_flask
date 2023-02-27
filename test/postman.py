import requests

def print_response(response):
    print(response.status_code) # ステータスコードを表示
    print(response.headers) # レスポンスヘッダーを表示
    print(response.text) # レスポンスボディを表示

def login(user_id):
    payload = {
        'user_id': user_id,
        'password': 'hogepiyo'
    }
    url = 'http://127.0.0.1:5098/account/login'
    response = requests.post(url, json=payload)
    print_response(response)
    # print(response.headers["Set-Cookie"])
    cookie = response.headers["Set-Cookie"]
    session_id = cookie.split(";")[0].replace("session=","")
    print("login:", session_id)
    return session_id

def check_login(session_id):
    session = requests.session()
    cookie = {"session": session_id}
    session.cookies.update(cookie)
    url = 'http://127.0.0.1:5098/account/check_login'
    response = session.get(url)
    print(response.text)
    # print_response(response)

if __name__ == '__main__':
    session_id = login('takaken1991')
    # check_login(session_id)
    # check_login("cookie_value")
    # check_login(session_id)

    # session_id = login('takaken1992')
    # check_login(session_id)


    