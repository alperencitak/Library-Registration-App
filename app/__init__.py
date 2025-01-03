from flask import Flask
from .models.base import db
from config import Config
from flask_migrate import Migrate
from .api.auth_api import auth_bp
from .api.category_api import category_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .models import base, user, book, bookcategory, category, loan, author

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(category_bp, url_prefix="/category")

    Migrate(app, db)

    return app
