from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    id = fields.Int()
    name = fields.String(required=True, validate=validate.Length(min=2, max=40))
    surname = fields.String(required=True, validate=validate.Length(min=2, max=40))
    role = fields.String(required=True, validate=validate.OneOf(["staff", "member"]))
    phone = fields.String(required=True, validate=validate.Length(min=10, max=20))
    email = fields.Email(required=True)


class UserRegisterSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=2, max=40))
    surname = fields.String(required=True, validate=validate.Length(min=2, max=40))
    role = fields.String(required=True, validate=validate.OneOf(["staff", "member"]))
    phone = fields.String(required=True, validate=validate.Length(min=10, max=20))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8), load_only=True)


class UserLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(
        required=True,
        validate=validate.Length(min=8),
        load_only=True
    )
