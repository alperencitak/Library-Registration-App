from .base import db, BaseModel


class Book(BaseModel):
    __tablename__ = "books"

    title = db.Column(db.String(100), nullable=False)
    page_count = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    author = db.relationship("Author", back_populates="books")
    categories = db.relationship("Category", secondary="book_categories", back_populates="books")
