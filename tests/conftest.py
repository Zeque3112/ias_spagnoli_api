import pytest

from app.init import create_app
from app.models.user import users

@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        yield client

@pytest.fixture
def clear_users():
    users.clear()