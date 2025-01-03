from .base import db


class BookCategory(db.Model):
    __tablename__ = "book_categories"

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), primary_key=True)
