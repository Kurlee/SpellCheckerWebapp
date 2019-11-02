import os
import pytest
from SpellCheckApp import db, create_app
from flask import current_app
from SpellCheckApp.models import User, Post
from SpellCheckApp import db as _db
from config import basedir



"""
@pytest.fixture(scope='module')
def client():
    db_fd, current_app.config['DATABASE'] = tempfile.mkstemp()
    current_app.config['TESTING'] = True

    with current_app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(current_app.config['DATABASE'])
"""


@pytest.fixture(scope='module')
def new_user():
    user = User(username='withphone', two_fa='1234567891')
    return user


@pytest.fixture(scope='module')
def app(request):
    app = create_app('config.TestingConfig')
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='module')
def db(app, request):
    TESTDB = 'data-test.sqlite'
    TESTDB_PATH = os.path.join(basedir, TESTDB)
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    def teardown():
        _db.drop_all()
        os.unlink(TESTDB_PATH)

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='module')
def session(db, request):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope='module')
def test_client():
    flask_app = current_app('config.TestingConfig')

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()
