from SpellCheckApp import db
from datetime import datetime
from SpellCheckApp.forms import RegistrationForm, LoginForm, SubmissionForm, LoginHistory, QueryHistory
from SpellCheckApp.models import User, Post, History
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
        user.set_creation_time(datetime.utcnow())
        db.session.add(user)
        db.session.commit()
        flash(u'success', 'success')
        return redirect(url_for('spell_check.login'))

    return render_template('register.html', title='Register', form=form)


@spell_check.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('spell_check.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Incorrect username or password', "result")
            return redirect(url_for('spell_check.login'))

        if user.two_fa != form.two_fa.data:
            flash('failure to authenticate Two-factor', 'result')
            return redirect(url_for('spell_check.login'))

        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = "index"
        flash("success", "result")

        """ Create login history entry """
        hist = History(login_time=datetime.utcnow(), user_id=current_user.id)
        db.session.add(hist)
        db.session.commit()
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@spell_check.route('/logout')
def logout():
    """ Get the most recent login entry, and set the logout time """
    hist = current_user.history.order_by(History.id.desc()).first()
    hist.set_logout_time(datetime.utcnow())
    db.session.add(hist)
    db.session.commit()
    logout_user()
    return redirect(url_for('spell_check.index'))


@spell_check.route('/spell_check', methods=['GET', 'POST'])
@login_required
def submission():
    form = SubmissionForm()
    if form.validate_on_submit():
        current_user.increment_query_num()
        post = Post(body=form.inputtext.data, user_id=current_user.id)
        post.set_result()
        db.session.add(post)
        db.session.commit()
        flash('Submission successful!')
        return render_template("submission.html", title='Submit text', form=form, post=post)
    return render_template("submission.html", title='Submit text', form=form)


@spell_check.route('/history', methods=['GET', 'POST'])
@login_required
def history():
    if current_user.get_is_admin():
        users = User.query.all()
        form = QueryHistory()
        if form.validate_on_submit():
            requested_user = User.query.filter_by(username=form.username.data).first()
            requested_user_posts = requested_user.post.all()
            return render_template('history.html', posts=requested_user_posts, user=requested_user)
        return render_template('admin_history.html', form=form,  users=users)

    else:
        posts = current_user.post.all()
        title = current_user.username + "'s Submission History"
        return render_template('history.html', title=title, posts=posts, user=current_user)


@spell_check.route('/history/query<int:post_id>', methods=['GET'])
@login_required
def query(post_id):
    try:
        post = Post.query.get(post_id)
        post_author = post.get_author()
        if post_author == current_user.username or current_user.get_is_admin():
            return render_template("queryid.html", post=post)
        else:
            return render_template("forbidden.html")
    except:
        return render_template("forbidden.html")


@spell_check.route('/login_history', methods=['GET', 'POST'])
@login_required
def login_history():
    if current_user.get_is_admin():
        form = LoginHistory()
        users = User.query.all()
        if form.validate_on_submit():
            user = User.query.get(form.userid.data)

            return render_template("admin.html", title="Admin Panel", form=form, users=users, user=user)
        return render_template('admin.html', title="Admin Panel", form=form, users=users)
    else:
        return render_template('forbidden.html')



@spell_check.before_request
def before_request():
    pass
