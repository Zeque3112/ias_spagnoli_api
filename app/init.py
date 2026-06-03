from flask import Flask

from app.config import Config
from app.db import db

from app.routes.health import health_bp
from app.routes.users import user_bp

def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(health_bp)
    app.register_blueprint(user_bp)

    return app