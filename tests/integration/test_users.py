def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200

def test_create_user(client):
    response = client.post(
        "/users",
        json={
            "name": "Ezequiel"
        }
    )

    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Ezequiel"

def test_delete_user(client):
    create_response = client.post(
        "/users",
        json={
            "name": "Ezequiel"
        }
    )

    user_id = create_response.get_json()["id"]

    response = client.delete(f"/users/{user_id}")

    assert response.status_code == 200