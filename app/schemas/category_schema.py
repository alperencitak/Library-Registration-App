from marshmallow import Schema, fields, validate


class CategorySchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=3, max=120))
