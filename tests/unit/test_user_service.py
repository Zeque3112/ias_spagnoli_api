from app.models.user import User
from app.db import db
from app.services.user_service import get_users, create_user, delete_user

def test_create_user(app):

    user = create_user("Ezequiel")

    assert user.id == 1
    assert user.name == "Ezequiel"

def test_get_users(app):

    user = User(name="Ezequiel")

    db.session.add(user)
    db.session.commit()

    result = get_users()

    assert len(result) == 1
    assert result[0].name == "Ezequiel"

def test_delete_existing_user(app):

    user = User(name="Ezequiel")

    db.session.add(user)
    db.session.commit()

    result = delete_user(user.id)

    assert result is True

    assert User.query.count() == 0

def test_delete_non_existing_user(app):

    result = delete_user(999)

    assert result is False