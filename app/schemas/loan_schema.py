from marshmallow import Schema, fields, validate


class LoanSchema(Schema):
    id = fields.Integer()
    book_id = fields.Integer(required=True, load_only=True)
    user_id = fields.Integer(required=True, load_only=True)
    loan_date = fields.DateTime()
    return_date = fields.DateTime()
    due_date = fields.DateTime(required=True)
    status = fields.Boolean()

    book = fields.Nested("BookSchema", dump_only=True)
    user = fields.Nested("UserSchema", dump_only=True)
