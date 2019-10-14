from sqlalchemy import Column
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from SpellCheckApp import db, login, DevelopmentConfig
from flask_login import UserMixin
from subprocess import check_output
from hashlib import sha256
import os

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username: Column = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    two_fa: Column = db.Column(db.String(14))
    post = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, 'pbkdf2:sha256', 20)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    result = db.Column(db.Text)

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    def set_result(self, body):
        # get hash of the post for file name
        hash_object = sha256(body.encode('utf-8'))
        filename = hash_object.hexdigest()
        file_path = os.path.join(DevelopmentConfig.UPLOADS_DIR, filename)

        # save the post to a file in order to pass to spell checker
        f = open(file_path, "w+")
        f.write(body)
        f.close()

        """     Example Command
        /home/admin/PycharmProjects/untitled/SpellCheckApp/static/a.out 
        /home/admin/PycharmProjects/untitled/SpellCheckApp/static/dictionary_file 
        -c /home/admin/PycharmProjects/untitled/SpellCheckApp/static/uploads/filename
        """
        result = check_output([DevelopmentConfig.STATIC_DIR + "/a.out",
                               DevelopmentConfig.STATIC_DIR + "/dictionary_file",
                               "-c",
                               DevelopmentConfig.UPLOADS_DIR + "/" + filename
                               ])
        print(result.decode("utf-8"))
        self.result = result.decode("utf-8")


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
