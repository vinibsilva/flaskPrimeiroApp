from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flasgger import Swagger

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    with app.app_context():
        from .models import book_model
        db.create_all()
        Swagger(app)

        from .routes.book_routes import book_bp
        app.register_blueprint(book_bp)

    return app
