from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_script import Manager

""" Config """

db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
manager = Manager()
login.login_view = 'spell_check.login'

""" Initialize extensions """


def initialize_extensions(app):
    from .models import User, Post
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)
    manager.add_command('db', MigrateCommand)


""" Application Factory """


def create_app(config_filename = 'config.ProductionConfig'):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    initialize_extensions(app)
    from .routes import spell_check
    from . import models, routes
    app.register_blueprint(spell_check)
    return app


this_app = create_app()
