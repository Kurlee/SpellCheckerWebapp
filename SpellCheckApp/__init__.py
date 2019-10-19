from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



"""initialize the application"""
app = Flask(__name__)
app.config.from_object(Config)


"""Initialize plugins"""
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
from SpellCheckApp import routes, models

# db.create_all()
# db.session.commit()


