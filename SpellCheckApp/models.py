from sqlalchemy import Column
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from SpellCheckApp import db, login
from flask import current_app
from flask_login import UserMixin
from subprocess import check_output
from tempfile import NamedTemporaryFile


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: Column = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    two_fa: Column = db.Column(db.String(14))
    creation_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post = db.relationship('Post', backref='author', lazy='dynamic')
    history = db.relationship('History', backref='event_owner', lazy='dynamic')
    total_query_num = db.Column(db.Integer, default=0)
    is_admin = db.Column(db.Boolean)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, 'pbkdf2:sha256', 20)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_creation_time(self, time):
        self.creation_time = time

    def get_creation_time(self):
        return self.creation_time

    def get_id(self):
        return str(self.id)

    def get_two_fa(self):
        return self.two_fa

    def get_username(self):
        return self.username

    def set_query_num(self, number_of_queries):
        self.total_query_num = number_of_queries

    def increment_query_num(self):
        self.total_query_num = self.total_query_num + 1

    def get_query_num(self):
        return self.total_query_num

    def get_is_admin(self):
        return self.is_admin

    def set_is_admin(self, priv_mod):
        self.is_admin = priv_mod

    def __repr__(self):
        return '<User {}>'.format(self.username)


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    logout_time = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<History - EID:{}, UID:{}, Login:{}, Logout{}>'.format(
            self.id, self.user_id, self.login_time, self.logout_time)

    def get_eid(self):
        return str(self.id)

    def get_uid(self):
        return str(self.user_id)

    def set_login_time(self, time):
        self.login_time = time

    def get_login_time(self):
        return self.last_login_time

    def set_logout_time(self, time):
        self.logout_time = time

    def get_logout_time(self):
        return self.last_logout_time


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    result = db.Column(db.Text)

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    def set_result(self):
        STATIC_DIR = current_app.config['STATIC_DIR']
        UPLOADS_DIR = current_app.config['UPLOADS_DIR']
        # get hash of the post for file name
        fp = NamedTemporaryFile(mode="w+", dir=UPLOADS_DIR)

        # hash_object = sha256(self.body.encode('utf-8'))
        # filename = hash_object.hexdigest()
        # file_path = path.join(UPLOADS_DIR, filename)

        # save the post to a file in order to pass to spell checker
        # f = open(file_path, "w+")
        fp.write(self.body)
        fp.seek(0)

        """     Example Command
        Usage: ./program to_check.txt wordlist.txt
        """
        result = check_output([STATIC_DIR + "/a.out",
                               fp.name,
                               STATIC_DIR + "/dictionary_file"
                               ])
        print (result)
        self.result = result.decode("utf-8")

        # Delete temporary file after passing to the spell checker
        fp.close()

    def get_result(self):
        return self.result

    def get_timestamp(self):
        return self.timestamp

    def get_author(self):
        return User.query.get(self.user_id).username

    # edit body of the post
    # TODO : create timestamp to track the last edit time
    def set_body(self, edited_body):
        self.body = edited_body
        self.set_result()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
