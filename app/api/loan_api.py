from flask import Blueprint, request, jsonify
from ..services.loan_service import LoanService

loan_bp = Blueprint('loan_api', __name__)


@loan_bp.route("/")
def get_all():
    return jsonify(LoanService.get_all()), 200


@loan_bp.route("/id")
def get_by_id():
    loan_id = request.args.get('id')
    return jsonify(LoanService.get_by_id(loan_id)), 200


@loan_bp.route("/user-id")
def get_by_user_id():
    user_id = request.args.get('id')
    return jsonify(LoanService.get_by_user_id(user_id)), 200


@loan_bp.route("/book-id")
def get_by_book_id():
    book_id = request.args.get('id')
    return jsonify(LoanService.get_by_book_id(book_id)), 200


@loan_bp.route("/add", methods=['POST'])
def add():
    data = request.get_json()
    return jsonify(LoanService.add(data)), 200


@loan_bp.route("/delete", methods=['DELETE'])
def delete():
    loan_id = request.args.get('id')
    return jsonify(LoanService.delete_by_id(loan_id)), 200


@loan_bp.route("/update", methods=['PATCH'])
def update():
    data = request.get_json()
    return jsonify(LoanService.update(data)), 200
