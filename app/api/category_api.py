from flask import request, jsonify, Blueprint
from ..services.category_service import CategoryService

category_bp = Blueprint("category_api", __name__)


@category_bp.route("/")
def get_all():
    return jsonify(CategoryService.get_all()), 200


@category_bp.route("/search")
def get_all_by_character():
    query = request.args.get('q', '')
    try:
        categories = CategoryService.get_all_by_character(query)
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@category_bp.route("/add", methods=['POST'])
def add_category():
    data = request.get_json()
    return jsonify(CategoryService.add_category(data)), 200


@category_bp.route("/delete", methods=['DELETE'])
def delete_category():
    category_id = request.args.get("id")
    return jsonify(CategoryService.delete_category_by_id(category_id))
