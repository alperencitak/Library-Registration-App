from ..schemas.loan_schema import LoanSchema
from ..models.base import db
from ..models.loan import Loan


class LoanService:

    @staticmethod
    def get_all():
        loans = Loan.query.all()
        schema = LoanSchema(many=True)
        return schema.dump(loans)

    @staticmethod
    def get_by_id(loan_id):
        loan = Loan.query.filter_by(id=loan_id).first()
        schema = LoanSchema()
        if loan:
            return schema.dump(loan)
        else:
            return {"error": f"Loan not found by id: {loan_id}"}

    @staticmethod
    def get_by_user_id(user_id):
        loans = Loan.query.filter_by(user_id=user_id).all()
        schema = LoanSchema(many=True)
        if loans:
            return schema.dump(loans)
        else:
            return {"error": f"Loan not found by user id: {user_id}"}

    @staticmethod
    def get_by_book_id(book_id):
        loans = Loan.query.filter_by(book_id=book_id).all()
        schema = LoanSchema(many=True)
        if loans:
            return schema.dump(loans)
        else:
            return {"error": f"Loan not found by book id: {book_id}"}

    @staticmethod
    def add(data):
        schema = LoanSchema()
        validated_data = schema.load(data)

        loan = Loan(
            book_id=validated_data['book_id'],
            user_id=validated_data['user_id'],
            due_date=validated_data['due_date']
        )

        db.session.add(loan)
        db.session.commit()

        return schema.dump(loan)

    @staticmethod
    def delete_by_id(loan_id):
        schema = LoanSchema()
        loan = Loan.query.filter_by(id=loan_id).first()

        if loan:
            db.session.delete(loan)
            db.session.commit()
            return {"message": "Delete successful."}
        else:
            return {"error": f"Loan not found by id: {loan_id}"}

    @staticmethod
    def update(data):
        schema = LoanSchema(partial=True)
        validated_data = schema.load(data, partial=True)
        loan_id = validated_data['id']
        loan = Loan.query.get(loan_id)
        if not loan:
            raise {"error": f"Loan not found by id: {loan_id}"}

        for key, value in validated_data.items():
            setattr(loan, key, value)

        db.session.commit()

        return schema.dump(loan)
