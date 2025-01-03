from marshmallow import Schema, fields, validate


class BookSchema(Schema):
    id = fields.Integer()
    title = fields.String(required=True, validate=validate.Length(min=3, max=100))
    page_count = fields.Integer(required=True)
    author_id = fields.Integer(required=True)
    category_ids = fields.List(fields.Integer(), load_only=True)
    categories = fields.Nested("CategorySchema", many=True, dump_only=True)
