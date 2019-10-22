import os
import tempfile
import pytest
from SpellCheckApp import db, create_app
from flask import current_app
from SpellCheckApp.models import User, Post


@pytest.fixture(scope='module')
def client():
    db_fd, current_app.config['DATABASE'] = tempfile.mkstemp()
    current_app.config['TESTING'] = True

    with current_app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(current_app.config['DATABASE'])


@pytest.fixture(scope='module')
def new_user():
    user = User(username='withphone', two_fa='1234567891')
    return user


@pytest.fixture(scope='module')
def init_database():
    gooduser1 = User(username='withphone', two_fa='1234567891')
    gooduser2 = User(username='withphone1', two_fa='9999999999')
    gooduser_nophone1 = User(username='nophone', two_fa='')

    post1_clean = Post(body="This text has no misspellings")
    post2_clean = Post(body="This text has no misspellings and contains some symbols: ")
    post3_clean = Post(body="This text has no misspellings ")
    post4_clean = Post(body="This text has no misspellings")
    post1_dirty = Post(body="This text has one word misspelled: isntall")
    post2_dirty = Post(body="This text has one word misspelled: catsss")
    post3_dirty = Post(body="This text has basic xss: <script>alert(1)</script>")
    post4_dirty = Post(body="This text has an AFL test case:\
            =================== \
            AFL ting test cases \
            ========= \
              (See READwelcomegeneral il.) \
             \
            The arcs/, images/, multimedia/, and others/ sudirPcto contain small, \
            staniles that can be used to seed ars for a \
            vqriety oI common data formats. \
             \
            There is proÑably noth to be said about,tes, pt that themized for size and stripped of any nonential fluf∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑∑f. Some directories \
            contain sse varioˇ fÄ Ëres of the unÜerlying format. \
            For example, there is a PNG file with and wihouwelcomeor profile.ˇ \
            Additionak˝test es \
            are always welcome. \
            en starting f   d Ò     fuzzing jåbs benefit from a\
            sma~l and concise dictionary.See ../dictioÜaries/README.dictionarieboutr more.")


    """ Commit users to the DB """
    db.create_all()
    db.session.commit()

    db.session.add(gooduser1)
    db.session.add(gooduser2)
    db.session.add(gooduser_nophone1)
    db.session.commit()

    """ Commit Posts to the DB """



    yield db

    db.drop_all()


@pytest.fixture(scope='module')
def test_client():
    flask_app = current_app('config.TestingConfig')

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


