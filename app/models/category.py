from .base import db, BaseModel


class Category(BaseModel):
    __tablename__ = "categories"

    name = db.Column(db.String(100), nullable=False)

    book_categories = db.relationship("BookCategory", back_populates="category")
