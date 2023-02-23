from database.user_database import Session, User
from werkzeug.security import generate_password_hash, check_password_hash

class AccountManager:
    def __init__(self):
        self.session = Session()

    def add_user(self, user_id, user_name, password, email):
        password = self.to_hash_password(password)
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
            password = self.to_hash_password(password)
            user.password = password
        self.session.commit()
        self.session.close()
        
    def delete_user(self, user_id):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        self.session.delete(user)
        self.session.commit()
        self.session.close()

    def to_hash_password(self, password):
        return generate_password_hash(password, method='sha512', salt_length=16)

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

def add_user():
    manager = AccountManager()
    manager.add_user('takaken1991', 'takahashi kenta', 'hogepiyo', 'kenta1991@gmail.com')

    manager = AccountManager()
    manager.add_user('wataru', 'takahashi wataru', 'password', 'wataru@gmail.com')

def get_user():
    manager = AccountManager()
    user = manager.get_user("ken1991")
    print(user.user_id, user.user_name, user.password, user.email)

def update_user():
    manager = AccountManager()
    # manager.update_user("ken1991", user_name='takahashi kenta', email="kenta@gmail.com")
    manager.update_user("ken1991", password='1234')

    # manager = AccountManager()
    # manager.update_user("wataru1970", user_name='wataru-takahashi', email="wataru1970@gmail.com")

def delete_user():
    manager = AccountManager()
    manager.delete_user("ken1991")

def get_all_users():
    manager = AccountManager()
    users = manager.get_all_users()
    for user in users:
        print(user.user_id, user.user_name, user.email)

def authenticate_user():
    manager = AccountManager()
    flg = manager.authenticate_user("ken1991", "1234")
    print(flg)

if __name__ == '__main__':
    # add_user()
    # update_user()
    # authenticate_user()
    pass








    
