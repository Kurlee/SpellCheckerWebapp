from SpellCheckApp import app
from flask import session, render_template, request, flash


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


@app.route('/register', methods=['POST'])
def create_user():
    return render_template('register.html')


@app.route('/login', methods=['POST'])
def do_login():
    return render_template('login.html')


