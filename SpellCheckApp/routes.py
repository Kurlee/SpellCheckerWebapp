from SpellCheckApp import forms
from flask import current_app, Blueprint, render_template, flash, redirect, url_for, session
app = Blueprint('app', __name__, url_prefix='/')


"""     
        1.User registration: /your/webroot/register
        2.User login: /your/webroot/login
        3.Two-factor authentication: /your/webroot/login
        4.Text submission: /your/webroot/spell_check
        5.Result retrieval: /your/webroot/spell_ch
"""


@app.route('/')
@app.route('/index')
def root():
    if not session.get('logged_in'):
        return render_template('register.html')
    else:
        return "hello <name>"


@app.route('/register', methods=['GET', 'POST'])
def create_user():
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def do_login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}' .format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', titile='Sign in', form=form)


