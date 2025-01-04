from marshmallow import fields, validate, Schema
from ..models.base import db


class AuthorSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=3, max=100))
    surname = fields.String(required=True, validate=validate.Length(min=3, max=80))
    books = fields.Nested("BookSchema", many=True, dump_only=True)
