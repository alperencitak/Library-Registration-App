from .base import db, BaseModel


class Author(BaseModel):
    __tablename__ = "authors"

    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(80), nullable=False)

    books = db.relationship("Book", back_populates="author")
