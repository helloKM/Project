from flask import Blueprint, render_template, request, session
from model.adv import adv_account

adv_bp = Blueprint('advter', __name__)


@adv_bp.route('/check_login', methods=['post'])
def check_login():
    phone = request.form['phone']
    password = request.form['password']
    advter = adv_account.query.filter_by(phone=phone).first()
    if advter == None:
        return '<script>alert("用户名或密码错误");location.href="/driver/login"</script>'
    else:
        if advter.check(password):
            session['adv_account_id'] = advter.account_ID
            session['adv_charge_name'] = advter.charge_name
            # 这里应该写个token
            return '<script>location.href="/adv/home"</script>'
        else:
            return '<script>alert("用户名或密码错误");location.href="/driver/login"</script>'


@adv_bp.route('/check_adv_submit')
def check_adv_submit():
    pass#前端有问题需要改

@adv_bp.route('/adv_submit')
def adv_submit():
    return render_template('Users module/ad_submit.html', name=session['adv_charge_name'])


@adv_bp.route('/login')
def login():
    return render_template('Users module/login.html')


@adv_bp.route('/home')
def home():
    return render_template('Users module/ad_home.html', name=session['adv_charge_name'])
