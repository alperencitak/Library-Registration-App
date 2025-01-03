from .base import db, BaseModel


class Category(BaseModel):
    __tablename__ = "categories"

    name = db.Column(db.String(100), nullable=False)

    books = db.relationship("Book", secondary="book_categories", back_populates="categories")
