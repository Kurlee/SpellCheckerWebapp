from sqlalchemy import Column
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from SpellCheckApp import db, login
from flask import current_app
from flask_login import UserMixin
from subprocess import check_output
from hashlib import sha256
from os import path
from tempfile import TemporaryFile


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: Column = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    two_fa: Column = db.Column(db.String(14))
    last_login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    last_logout_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, 'pbkdf2:sha256', 20)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

    def get_two_fa(self):
        return self.two_fa

    def get_username(self):
        return self.username

    def __repr__(self):
        return '<User {}>'.format(self.username)


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
        fp = TemporaryFile(dir=UPLOADS_DIR)

        # hash_object = sha256(self.body.encode('utf-8'))
        # filename = hash_object.hexdigest()
        # file_path = path.join(UPLOADS_DIR, filename)

        # save the post to a file in order to pass to spell checker
        # f = open(file_path, "w+")
        fp.write(self.body)

        """     Example Command
        Usage: ./program to_check.txt wordlist.txt
        """
        result = check_output([STATIC_DIR + "/a.out",
                               UPLOADS_DIR + "/" + fp,
                               STATIC_DIR + "/dictionary_file"
                               ])
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
