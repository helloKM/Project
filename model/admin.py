from app_config import db
import hashlib


class admin_account(db.Model):
    __tablename__ = 'admin_account'
    account_ID = db.Column('account_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    account_name = db.Column('account_name', db.String(30), nullable=False)
    salt = db.Column('salt', db.String(16), nullable=False)
    account_pwd = db.Column('account_pwd', db.String(40), nullable=False)

    def check(self, password):
        password = hashlib.md5((password + self.salt).encode('ascii')).hexdigest()
        if password == self.account_pwd:
            return True
        else:
            return False
