from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from movieApp.config import Config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from movieApp.main.routes import main
    from movieApp.admin.routes import admin

    app.register_blueprint(main)
    app.register_blueprint(admin)

    return app
