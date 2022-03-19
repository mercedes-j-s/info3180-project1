from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = "Som3$ec5etK*y"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:Password@localhost/Properties"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask-Login login manager
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# Instantiate Flask-Migrate library here
from app import views