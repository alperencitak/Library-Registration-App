from ..schemas.user_schema import UserSchema
from ..models.base import db
from ..models.user import User


class UserService:

    @staticmethod
    def get_all():
        users = User.query.all()
        schema = UserSchema(many=True)
        return schema.dump(users)

    @staticmethod
    def get_by_id(user_id):
        user = User.query.filter_by(id=user_id).first()
        schema = UserSchema()
        if user:
            return schema.dump(user)
        else:
            return ValueError(f"User not found by id: {user_id}")

    @staticmethod
    def update(data):
        schema = UserSchema(partial=True)
        validated_data = schema.load(data, partial=True)
        user_id = validated_data['id']
        user = User.query.get(user_id)
        if not user:
            raise ValueError(f"User not found by id: {user_id}")

        for key, value in validated_data.items():
            setattr(user, key, value)

        db.session.commit()

        return schema.dump(user)
