import os
import tempfile
import pytest
from SpellCheckApp import create_app


@pytest.fixture
def app():
    app = create_app('testing')
    return app
@pytest.fixture
def client():
    client = app.app.test_client()
    with app.app.context():
        app.init_db()

    yeild client




