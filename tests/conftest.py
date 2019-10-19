import os
import tempfile
import pytest
from SpellCheckApp import app, db
from SpellCheckApp.models import User, Post


@pytest.fixture(scope='module')
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


@pytest.fixture(scope='module')
def new_user():
    user = User(username='withphone', two_fa='1234567891')
    return user

@pytest.fixture(scope='module')
def init_database():
    gooduser1 = User(username='withphone', two_fa='1234567891')
    gooduser2 = User(username='withphone1', two_fa='9999999999')
    gooduser_nophone1 = User(username='nophone', two_fa='')

    db.create_all()
    db.session.commit()

    db.session.add(gooduser1)
    db.session.add(gooduser2)
    db.session.add(gooduser_nophone1)
    db.session.commit()

    yield db

    db.drop_all()
