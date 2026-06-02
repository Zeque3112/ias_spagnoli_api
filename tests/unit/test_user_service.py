from app.models.user import users
from app.services.user_service import get_users, create_user, delete_user

def test_create_user():
    users.clear()

    user = create_user("Ezequiel")

    assert user["id"] == 1
    assert user["name"] == "Ezequiel"

def test_get_users():
    users.clear()

    users.append({
        "id": 1,
        "name": "Ezequiel"
    })

    result = get_users()

    assert len(result) == 1
    assert result[0]["name"] == "Ezequiel"

def test_delete_existing_user():
    users.clear()

    users.append({
        "id": 1,
        "name": "Ezequiel"
    })

    result = delete_user(1)

    assert result == True
    assert len(users) == 0

def test_delete_non_existing_user():
    users.clear()

    result = delete_user(99)

    assert result == False