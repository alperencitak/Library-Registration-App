from flask import request, jsonify, Blueprint
from ..services.book_service import BookService

book_bp = Blueprint("book_api", __name__)


@book_bp.route("/")
def get_all():
    return BookService.get_all()


@book_bp.route("/id")
def get_by_id():
    book_id = request.args.get('id')
    try:
        book = BookService.get_by_id(book_id)
        return jsonify(book), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 500


@book_bp.route("/search")
def get_by_character():
    query = request.args.get('q', '')
    book = BookService.get_by_character(query)
    return jsonify(book), 200


@book_bp.route("/add", methods=['POST'])
def add():
    data = request.get_json()
    return BookService.add(data), 200


@book_bp.route("/delete", methods=['DELETE'])
def delete_by_id():
    book_id = request.args.get('id')
    try:
        return jsonify(BookService.delete_by_id(book_id))
    except ValueError as e:
        return jsonify({"error": str(e)})
