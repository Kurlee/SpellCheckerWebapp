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
        user = User(username=form.username.data, two_fa=form.two_fa.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering! Login, then navigate to the submit tab to submit your text!')
        message_type = "success"
        return render_template("index.html", message_type=message_type)
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    message_type = "result"
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Incorrect username or password')
            return render_template("login.html", form=form, message_type=message_type)

        if user.two_fa != form.two_fa.data:
            flash('failure to authenticate Two-factor')
            return render_template("login.html", form=form, message_type=message_type)

        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = "index"
        flash("success")
        return render_template(next_page, form=form, message_type=message_type)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/spell_check', methods=['GET', 'POST'])
@login_required
def submission():
    form = SubmissionForm()
    if form.validate_on_submit():
        post = Post(body=form.inputtext.data, user_id=current_user.id)
        post.set_result(form.inputtext.data)
        db.session.add(post)
        db.session.commit()
        flash('Submission successful!')
        return render_template("submission.html", title='Submit text', form=form, post=post)
    posts = Post.query.filter_by(user_id=current_user.id)
    return render_template("submission.html", title='Submit text', form=form)


def result(post):
    return render_template("result.html", post=post)


@app.route('/user')
def all_results():
    user = current_user
    posts = user.posts.all()
    return render_template(url_for('result'), posts=posts)
