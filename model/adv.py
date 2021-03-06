from app_config import db
import hashlib


class adv_info(db.Model):
    __tablename__ = 'adv_info'
    adv_ID = db.Column('adv_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    cost = db.Column('cost', db.DECIMAL(6, 3), nullable=False)
    amounts = db.Column('amounts', db.Integer, nullable=False)
    start_date = db.Column('start_date', db.DateTime, nullable=False)
    end_date = db.Column('end_date', db.DateTime)
    location1_X = db.Column('location1_X', db.Float, nullable=False)
    location1_Y = db.Column('location1_Y', db.Float, nullable=False)
    location2_X = db.Column('location2_X', db.Float, nullable=False)
    location2_Y = db.Column('location2_Y', db.Float, nullable=False)
    advter_account_ID = db.Column('advter_account_ID', db.Integer, nullable=False)
    adv_pic = db.Column('adv_pic', db.String(50))
    adv_text = db.Column('adv_text', db.String(80))


class adv_account(db.Model):
    __tablename__ = 'adv_account'
    account_ID = db.Column('account_ID', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    salt = db.Column('salt', db.String(16), nullable=False)
    account_pwd = db.Column('account_pwd', db.String(40), nullable=False)
    company_name = db.Column('company_name', db.String(40), nullable=False)
    adv_amount = db.Column('adv_amount', db.Integer, nullable=False)
    charge_name = db.Column('charge_name', db.String(18), nullable=False)
    phone = db.Column('phone', db.String(11), nullable=False)
    check_flag = db.Column('check_flag', db.Boolean)
    remark = db.Column('remark', db.String(50))

    def check(self, password):
        password = hashlib.md5((password + self.salt).encode('ascii')).hexdigest()
        if password == self.account_pwd:
            return True
        else:
            return False
