from datetime import datetime
from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok',
                    "service": "ias_apellido_api",
                    "timestamp": datetime.now()
                    }), 200