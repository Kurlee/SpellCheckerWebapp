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

    # UID 1
    gooduser1 = User(username='withphone', two_fa='1234567891')
    # UID 2
    gooduser2 = User(username='withphone1', two_fa='9999999999')
    # UID 3
    gooduser_nophone1 = User(username='nophone', two_fa='')
    body_clean1 = "This text has no misspellings"
    body_clean2 = "This text has no misspellings and contains some symbols: "
    body_clean_duplicate = "This text has no misspellings "
    body_dirty1 = "This text has one word misspelled: isntall"
    body_dirty2 = "This text has one word misspelled: catsss"
    body_dirty_xss = "This text has basic xss: <script>alert(1)</script>"
    body_dirty_afl = "This text has an AFL test case:\
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
                contain sse varioˇ fÄ Ëres of the unÜerlying format. \
                For example, there is a PNG file with and wihouwelcomeor profile.ˇ \
                Additionak˝test es \
                are always welcome. \
                en starting f   d Ò     fuzzing jåbs benefit from a\
                sma~l and concise dictionary.See ../dictioÜaries/README.dictionarieboutr more."
    post1_clean = Post(body=body_clean1, user_id=1)
    post2_clean = Post(body=body_clean2, user_id=2)
    post3_clean = Post(body=body_clean_duplicate, user_id=1)
    post1_dirty = Post(body=body_dirty1, user_id=2)
    post2_dirty = Post(body=body_dirty2, user_id=1)
    post3_dirty = Post(body=body_dirty_xss, user_id=3)
    post4_dirty = Post(body=body_dirty_afl, user_id=3)


    """ Commit users to the DB """
    db.create_all()
    db.session.commit()

    db.session.add(gooduser1)
    db.session.add(gooduser2)
    db.session.add(gooduser_nophone1)
    db.session.commit()

    """ Commit Posts to the DB """

    db.session.add(post1_clean)
    db.session.add(post2_clean)
    db.session.add(post3_clean)
    db.session.add(post1_dirty)
    db.session.add(post2_dirty)
    db.session.add(post3_dirty)
    db.session.add(post4_dirty)

    db.session.commit()

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


