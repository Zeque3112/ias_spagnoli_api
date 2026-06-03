from app.models.user import User
from app.db import db

def get_users():
    return User.query.all()

def create_user(name):

    user = User(name=name)

    db.session.add(user)
    db.session.commit()

    return user

from app.models.user import User
from app.db import db

def delete_user(user_id):

    user = db.session.get(User, user_id)

    if not user:
        return False

    db.session.delete(user)
    db.session.commit()

    return True