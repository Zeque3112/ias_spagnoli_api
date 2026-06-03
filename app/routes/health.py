from datetime import datetime
from flask import Blueprint, jsonify, current_app
from sqlalchemy import text
from app.db import db

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():

    try:
        db.session.execute(text("SELECT 1"))
        database_status = "up"

    except Exception:
        database_status = "down"


    return jsonify({
        "status": "ok",
        "service": "ias_spagnoli_api",
        "environment": current_app.config["ENV"],
        "database": database_status,
        "timestamp": datetime.now().isoformat()
    }), 200