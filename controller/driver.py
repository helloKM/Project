from flask import request, render_template, session, current_app, redirect, url_for, Blueprint
import os
from werkzeug.utils import secure_filename
from model import db
from model.driver import driver_account
import hashlib

app = current_app
driver_bp = Blueprint('driver', __name__)


@driver_bp.route('/')
def index():
    if 'driver_account_id' not in session:
        return redirect(url_for('driver.login'))
    else:
        return redirect(url_for('driver.home'))


@driver_bp.route('/check_login', methods=['POST'])
def check_login():
    phone = request.form['phone']
    password = request.form['password']
    driver = driver_account.query.filter_by(phone=phone).first()
    if driver == None:
        return '<script>alert("用户名或密码错误");location.href="/driver/login"</script>'
    else:
        if driver.check(password):
            session['driver_account_id'] = driver.account_ID
            session['driver_user_name'] = driver.user_name
            # 这里应该写个token
            return '<script>location.href="/driver/home"</script>'
        else:
            return '<script>alert("用户名或密码错误");location.href="/driver/login"</script>'


@driver_bp.route('/check_register', methods=['POST'])
def check_register():
    user_id = request.form['userID']
    phone = request.form['phone']
    user_name = request.form['user_name']
    password = request.form['password']
    ID_card_image = request.files['ID_card_image']
    permit_card_image = request.files['permit_card_image']
    car_image = request.files['car_image']
    ID_filename = secure_filename(ID_card_image.filename)
    permit_filename = secure_filename(permit_card_image.filename)
    ID_card_image.save(os.path.join(app.root_path, 'static/image/ID_card', ID_filename))
    permit_card_image.save(os.path.join(app.root_path, 'static/image/permit_card', permit_filename))
    car_pic_filename = secure_filename(car_image.filename)
    car_image.save(os.path.join(app.root_path, 'static/image/car', car_pic_filename))
    u = driver_account(phone, password, user_name, user_id, ID_filename, permit_filename, car_pic_filename)
    db.session.add(u)
    db.session.commit()
    return '<script>alert("注册成功!");location.href="/driver/login"</script>'


@driver_bp.route('/home')
def home():
    return render_template('Users module/home.html', name=session['driver_user_name'])


@driver_bp.route('/login')
def login():
    return render_template('Users module/login.html')


@driver_bp.route('/register')
def register():
    return render_template('Users module/create-account.html')
