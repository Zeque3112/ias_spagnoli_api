from app.models.user import users

def get_users():
    return users

def create_user(name: str):
    user = {
        "id": len(users) + 1,
        "name": name
    }

    users.append(user)
    return user

def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return True
        
    return False