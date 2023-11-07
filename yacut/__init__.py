from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import views, api_views, error_handlers
