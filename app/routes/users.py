from flask import Blueprint, jsonify, request

from app.services.user_service import (
    get_users,
    create_user,
    delete_user
)

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['GET'])
def gett_all_users():
    return jsonify(get_users()), 200

@user_bp.route('/users', methods=['POST'])
def create_new_user():
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({
            "message": "name is required"
        }), 400
    
    user = create_user(data['name'])
    return jsonify(user), 201

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    deleted = delete_user(user_id)

    if not deleted:
        return jsonify({
            "message": "User not found"
        }), 404
    
    return jsonify({
        "message": "User deleted successfully"
    }), 200