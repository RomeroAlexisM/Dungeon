
from flask_login import LoginManager

from api.app import app

DEBUG = True
SECRET_KEY = 'thisisasecret'
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.db'
CSRF_ENABLED = True
USER_ENABLE_EMAIL = False

