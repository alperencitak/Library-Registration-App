from flask import Flask
from .models.base import db
from config import Config
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .models import base, user, book, bookcategory, category, loan, author

    Migrate(app, db)

    return app
