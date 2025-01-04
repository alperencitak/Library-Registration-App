from ..schemas.author_schema import AuthorSchema
from ..models.author import Author
from ..models.base import db


class AuthorService:

    @staticmethod
    def get_all():
        authors = Author.query.all()
        schema = AuthorSchema(many=True)
        return schema.dump(authors)

    @staticmethod
    def get_by_id(author_id):
        author = Author.query.filter_by(id=author_id).first()
        schema = AuthorSchema()
        if author:
            return schema.dump(author)
        else:
            return ValueError(f"Author not found by id {author_id}")

    @staticmethod
    def get_by_character(query):
        authors = Author.query.filter(
            Author.name.ilike(f"%{query}%")
        ).order_by(Author.name).all()
        schema = AuthorSchema(many=True)
        return schema.dump(authors)

    @staticmethod
    def add(data):

        schema = AuthorSchema()
        validated_data = schema.load(data)

        author = Author(
            name=validated_data['name'],
            surname=validated_data['surname']
        )

        db.session.add(author)
        db.session.commit()

        return schema.dump(author)

    @staticmethod
    def delete_by_id(author_id):
        author = Author.query.filter_by(id=author_id).first()
        if author:
            db.session.delete(author)
            db.session.commit()
            return {"message": "Delete successful."}
        else:
            return ValueError(f"Author not found by id {author_id}")
