from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app(config_name):
    """initialize the application"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    """Initialize plugins"""
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'sc.login'

    """Set the context of the application and set routes"""
    with app.app_context():
        from . import routes, models
        db.create_all()
        db.session.commit()
        app.register_blueprint(routes.sc)
        return app


