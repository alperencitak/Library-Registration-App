from ..schemas.book_schema import BookSchema
from ..models.category import Category
from ..models.book import Book
from ..models.base import db


class BookService:

    @staticmethod
    def get_all():
        books = Book.query.all()
        schema = BookSchema(many=True)

        return schema.dump(books)

    @staticmethod
    def get_by_character(query):
        books = Book.query.filter(
            Book.title.ilike(f"%{query}%")
        ).order_by(Book.title).all()
        schema = BookSchema(many=True)

        return schema.dump(books)

    @staticmethod
    def get_by_id(book_id):
        book = Book.query.filter_by(id=book_id).first()
        schema = BookSchema()
        return schema.dump(book)

    @staticmethod
    def add(data):

        schema = BookSchema()
        validated_data = schema.load(data)

        category_ids = validated_data.get("category_ids", [])
        categories = Category.query.filter(Category.id.in_(category_ids)).all()

        book = Book(
            title=validated_data['title'],
            page_count=validated_data['page_count'],
            author_id=validated_data['author_id'],
            categories=categories
        )

        db.session.add(book)
        db.session.commit()

        return schema.dump(book)

    @staticmethod
    def delete_by_id(book_id):

        book = Book.query.filter_by(id=book_id).first()

        if book:
            db.session.delete(book)
            db.session.commit()
            return {"message": "Delete successful."}
        else:
            return ValueError(f"Book not found by id: {book_id}")
