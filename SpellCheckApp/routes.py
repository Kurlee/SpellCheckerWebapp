from jinja2 import TemplateNotFound
from SpellCheckApp import db, app
from SpellCheckApp.forms import RegistrationForm, LoginForm, SubmissionForm
from SpellCheckApp.models import User, Post
from flask import abort, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

"""     
        1.User registration: /your/webroot/register
        2.User login: /your/webroot/login
        3.Two-factor authentication: /your/webroot/login
        4.Text submission: /your/webroot/spell_check
        5.Result retrieval: /your/webroot/spell_ch
"""


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for(next_page))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/spell_check')
@login_required
def submission():
    form = SubmissionForm()
    if form.validate_on_submit():
        post = Post(body=form.inputtext.data, user_id=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Submission successful!')
        post.get_result(form.inputtext.data)
        db.session.add(post)
        db.session.commit()
        result()
    posts = Post.query.filter_by(user_id=current_user)
    return render_template(url_for('submission'), title='Submit text', form=form, posts=posts)


def result():
    user = current_user
    post = user.posts.first()
    return render_template(url_for('result'), posts=post)


@app.route('/user')
def all_results():
    user = current_user
    posts = user.posts.all()
    return render_template(url_for('result'), posts=posts)
