from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from SpellCheckApp.routes import spell_check


""" Config """


db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
login.login_view = 'login'


""" Initialize extensions """


def initialize_extensions(app):
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)



""" Application Factory """


def create_app(config_filename=None):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    initialize_extensions(app)
    app.register_blueprint(spell_check)
    return app


"""
app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
from SpellCheckApp import routes, models

# db.create_all()
# db.session.commit()
"""
