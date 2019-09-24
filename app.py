from flask import Flask
from flask import session, render_template, request, flash
import os

app = Flask(__name__)

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
    user = {'username', 'Adrian'}       # user for testing, remove
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "hello <name>"


@app.route('/register', methods=['POST'])
def create_user():
    return root()


@app.route('/login', methods=['POST'])
def do_login():
    admin_request = False

    if request.form['username'] == 'admin':
        admin_request = True
    if request.form['password'] == 'password' and request.form['username'] == 'username':
        session['logged_in'] = True
        if admin_request:
            session['is_admin'] = True
    else:
        flash('username does not exist or supplied password incorrect for this user')
    return root()


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
