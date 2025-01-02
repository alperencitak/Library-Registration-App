from flask import Blueprint, request, jsonify
from ..services.auth_service import AuthService

auth_bp = Blueprint('auth_api', __name__)


@auth_bp.route("/register", methods=['POST'])
def register():
    data = request.get_json()

    try:
        response = AuthService.register_user(data)
        return jsonify(response), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@auth_bp.route("/login", methods=['POST'])
def login():
    data = request.get_json()

    try:
        response = AuthService.login_user(data)
        return jsonify(response), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
