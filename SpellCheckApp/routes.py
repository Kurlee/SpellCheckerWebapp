from jinja2 import TemplateNotFound
from SpellCheckApp import db
from SpellCheckApp.forms import RegistrationForm, LoginForm
from SpellCheckApp.models import User
from flask import abort, Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

sc = Blueprint('sc', __name__, template_folder='templates', static_folder='static')

"""     
        1.User registration: /your/webroot/register
        2.User login: /your/webroot/login
        3.Two-factor authentication: /your/webroot/login
        4.Text submission: /your/webroot/spell_check
        5.Result retrieval: /your/webroot/spell_ch
"""


@sc.route('/', defaults={'page': 'index'})
@sc.route('/index')
@login_required
def show(page):
    try:
        return render_template('/%s.html' % page)
    except TemplateNotFound:
        abort(404)


@sc.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering! Login, then navigate to the submit tab to submit your text!')
        return redirect((url_for('login')))
    return render_template('register.html', title='Register', form=form)


@sc.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('sc.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@sc.route('/logout')
def logout():
    logout_user()
    return  redirect(url_for('index'))
