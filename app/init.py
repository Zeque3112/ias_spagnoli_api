from flask import Flask

from app.routes.health import health_bp
from app.routes.users import user_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(health_bp)
    app.register_blueprint(user_bp)
    
    return app