from ..schemas.category_schema import CategorySchema
from ..models.base import db
from ..models.category import Category


class CategoryService:

    @staticmethod
    def add_category(data):

        schema = CategorySchema()
        validated_data = schema.load(data)

        category = Category(
            name=validated_data['name']
        )

        db.session.add(category)
        db.session.commit()

        return {"id": category.id, "name": category.name}

    @staticmethod
    def delete_category_by_id(category_id):
        category = Category.query.filter_by(id=category_id).first()
        if category:
            db.session.delete(category)
            db.session.commit()
            return {"message": "Delete successful."}
        else:
            return ValueError(f"Category not found by id {category_id}")

    @staticmethod
    def get_all():
        category_list = Category.query.order_by(Category.name).all()
        schema = CategorySchema(many=True)
        return schema.dump(category_list)

    @staticmethod
    def get_all_by_character(query):
        schema = CategorySchema(many=True)

        category_list = Category.query.filter(
            Category.name.ilike(f"%{query}%")
        ).order_by(Category.name).all()

        return schema.dump(category_list)
