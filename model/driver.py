from . import security
import hashlib
from app_config import db
import hashlib


class driver_account(db.Model):
    __tablename__ = 'driver_account'
    account_ID = db.Column('account_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    account_pwd = db.Column('account_pwd', db.String(40), nullable=False)
    salt = db.Column('salt', db.String(16), nullable=False)
    phone = db.Column('phone', db.String(11), nullable=False)
    account_money = db.Column('account_money', db.DECIMAL(10, 3), nullable=False)
    email = db.Column('email', db.String(60))
    check_flag = db.Column('check_flag', db.Boolean)
    deposit = db.Column('deposit', db.DECIMAL(6, 2), nullable=False)
    pad_flag = db.Column('pad_flag', db.Boolean)
    user_name = db.Column('user_name', db.String(18))
    user_ID = db.Column('user_id', db.String(20))
    card_pic = db.Column('card_pic', db.String(255))
    permit_pic = db.Column('permit_pic', db.String(255))
    car_pic = db.Column('car_pic', db.String(255))
    token = db.Column('token', db.String(40))

    def __init__(self, phone, password, user_name, user_id, card_pic, permit_pic, car_pic, email=None):
        self.salt = security.get_salt(16)
        self.account_pwd = hashlib.md5((password + self.salt).encode('ascii')).hexdigest()
        self.phone = phone
        self.account_money = 0
        self.email = email
        self.check_flag = None
        self.deposit = 0
        self.user_ID = user_id
        self.user_name = user_name
        self.card_pic = card_pic
        self.permit_pic = permit_pic
        self.car_pic = car_pic

    def check(self, password):
        password = hashlib.md5((password + self.salt).encode('ascii')).hexdigest()
        if password == self.account_pwd:
            return True
        else:
            return False
