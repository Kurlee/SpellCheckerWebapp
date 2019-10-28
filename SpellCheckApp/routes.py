from SpellCheckApp import db
from datetime import datetime
from SpellCheckApp.forms import RegistrationForm, LoginForm, SubmissionForm
from SpellCheckApp.models import User, Post
from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

spell_check = Blueprint('spell_check', __name__, template_folder='templates')

"""     
        1.User registration: /your/webroot/register
        2.User login: /your/webroot/login
        3.Two-factor authentication: /your/webroot/login
        4.Text submission: /your/webroot/spell_check
        5.Result retrieval: /your/webroot/spell_ch
"""


@spell_check.route('/')
@spell_check.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@spell_check.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('spell_check.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # no phone number supplied
        if form.two_fa.data is None:
            user = User(username=form.username.data)
        # phone number supplied
        else:
            sanitized_phone_number = form.two_fa.data.strip(' ()-')
            user = User(username=form.username.data, two_fa=sanitized_phone_number)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(u'success', 'success')
        return redirect(url_for('spell_check.login'))

    return render_template('register.html', title='Register', form=form)


@spell_check.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Incorrect username or password', "result")
            return redirect(url_for('spell_check.login'))

        if user.two_fa != form.two_fa.data:
            flash('failure to authenticate Two-factor', 'result')
            return redirect(url_for('spell_check.login'))

        user.last_login_time = datetime.utcnow()
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = "index"
        flash("success", "result")
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@spell_check.route('/logout')
def logout():
    current_user.last_logout_time = datetime.utcnow()
    db.session.commit()
    logout_user()
    return redirect(url_for('spell_check.index'))


@spell_check.route('/spell_check', methods=['GET', 'POST'])
@login_required
def submission():
    form = SubmissionForm()
    if form.validate_on_submit():
        post = Post(body=form.inputtext.data, user_id=current_user.id)
        post.set_result()
        db.session.add(post)
        db.session.commit()
        flash('Submission successful!')
        return render_template("submission.html", title='Submit text', form=form, post=post)
    return render_template("submission.html", title='Submit text', form=form)


@spell_check.before_request
def before_request():
    pass
