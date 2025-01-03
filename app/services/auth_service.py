from ..models.user import User
from passlib.hash import argon2
from ..models.base import db
from ..schemas.user_schema import UserRegisterSchema, UserLoginSchema


class AuthService:

    @staticmethod
    def register_user(data):

        schema = UserRegisterSchema()
        validated_data = schema.load(data)

        if User.query.filter_by(email=validated_data['email']).first():
            raise ValueError("Email has already taken")

        hashed_password = argon2.hash(validated_data['password'])

        user = User(
            name=validated_data['name'],
            surname=validated_data['surname'],
            role=validated_data['role'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return {"message": "User registered Successfully."}

    @staticmethod
    def login_user(data):

        schema = UserLoginSchema()
        validated_data = schema.load(data)

        user = User.query.filter_by(email=validated_data['email']).first()

        if user and argon2.verify(validated_data['password'], user.password):
            return {"user_id": user.id, "email": user.email}
        else:
            return ValueError("Invalid email or password")
