from .base import db, BaseModel


class User(BaseModel):
    __tablename__ = "users"

    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # staff - member
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
