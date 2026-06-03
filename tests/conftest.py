import pytest

from app.db import db
from app.init import create_app
from app.config import TestConfig


@pytest.fixture
def app():

    app = create_app(TestConfig)

    with app.app_context():

        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):

    return app.test_client()