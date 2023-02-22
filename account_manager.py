from database.user_database import Session, User
from werkzeug.security import check_password_hash
import hashlib

class AccountManager:
    def __init__(self):
        self.session = Session()
    
    def hash_password(password):
        # 文字列をバイト列に変換
        password_bytes = password.encode('utf-8')
        # SHA-256アルゴリズムでハッシュ化
        hashed_bytes = hashlib.sha256(password_bytes).digest()
        # ハッシュ化されたバイト列を16進数の文字列に変換して返す
        return hashed_bytes.hex()

        
    def add_user(self, user_id, user_name, password, email):
        user = User(user_id=user_id, user_name=user_name, email=email, password=password)
        self.session.add(user)
        self.session.commit()
        self.session.close()

    def get_user(self, user_id):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        self.session.close()
        return user

    def get_all_users(self):
        users = self.session.query(User).all()
        self.session.close()
        return users

    def update_user(self, user_id, user_name=None, password=None, email=None):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        if user_name:
            user.user_name = user_name
        if email:
            user.email = email
        if password:
            user.password = password
        self.session.commit()
        self.session.close()
        
    def delete_user(self, user_id):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        self.session.delete(user)
        self.session.commit()
        self.session.close()

    def authenticate_user(self, user_id, password):
        # ユーザーIDが存在するかチェックする
        user = self.get_user(user_id)
        if user is None:
            return False
        
        # パスワードが正しいかチェックする
        if check_password_hash(user.password, password):
            return True
        else:
            return False

if __name__ == '__main__':
    pass

    # manager = AccountManager()
    # manager.add_user('ken1991', 'takahashi kenta', '1234', 'kenta@gmail.com')

    # manager = AccountManager()
    # user = manager.get_user("ken1991")
    # print(user.user_id, user.user_name, user.password, user.email)

    # manager = AccountManager()
    # manager.update_user("ken1991", user_name='takahashi kenta', email="kenta@gmail.com")

    # manager = AccountManager()
    # manager.delete_user("ken1991")

    # manager = AccountManager()
    # manager.add_user('wataru', 'takahashi wataru', '5678', 'wataru@gmail.com')

    # manager = AccountManager()
    # manager.update_user("wataru1970", user_name='wataru-takahashi', email="wataru1970@gmail.com")

    # manager = AccountManager()
    # users = manager.get_all_users()
    # for user in users:
    #     print(user.user_id, user.user_name, user.email)

    password = '1234'

    


    # 文字列をバイト列に変換
    password_bytes = password.encode('utf-8')
    # SHA-256アルゴリズムでハッシュ化
    hashed_bytes = hashlib.sha256(password_bytes).digest()
    # ハッシュ化されたバイト列を16進数の文字列に変換して返す
    hashed_password = hashed_bytes.hex()

    print(check_password_hash(hashed_password, password))





    
