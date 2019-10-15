from SpellCheckApp import db, app
from SpellCheckApp.forms import RegistrationForm, LoginForm, SubmissionForm
from SpellCheckApp.models import User, Post
from flask import render_template, flash, redirect, url_for, request
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
        # no phone number supplied
        if form.two_fa.data is None:
            user = User(username=form.username.data)
        # phone number supplied
        else:
            user = User(username=form.username.data, two_fa=form.two_fa.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(u'Thank you for registering! Login, then navigate to the submit tab to submit your text!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Incorrect username or password', "result")
            return redirect(url_for('login'))

        if user.two_fa != form.two_fa.data:
            flash('failure to authenticate Two-factor', 'result')
            return redirect(url_for('login'))

        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = "index"
        flash("success", "result")
        return redirect(next_page)
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
        post.set_result()
        db.session.add(post)
        db.session.commit()
        flash('Submission successful!')
        return render_template("submission.html", title='Submit text', form=form, post=post)
    return render_template("submission.html", title='Submit text', form=form)


