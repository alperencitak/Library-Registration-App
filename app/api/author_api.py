from flask import request, jsonify, Blueprint
from ..services.author_service import AuthorService

author_bp = Blueprint("author_api", __name__)


@author_bp.route("/")
def get_all():
    return AuthorService.get_all()


@author_bp.route("/id")
def get_by_id():
    author_id = request.args.get('id')
    try:
        author = AuthorService.get_by_id(author_id)
        return jsonify(author), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 500


@author_bp.route("/search")
def get_by_character():
    query = request.args.get('q', '')
    author = AuthorService.get_by_character(query)
    return jsonify(author), 200


@author_bp.route("/add", methods=['POST'])
def add():
    data = request.get_json()
    return AuthorService.add(data), 200


@author_bp.route("/delete", methods=['DELETE'])
def delete_by_id():
    author_id = request.args.get('id')
    try:
        return jsonify(AuthorService.delete_by_id(author_id))
    except ValueError as e:
        return jsonify({"error": str(e)})
