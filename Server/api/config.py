from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DEBUG = True
SECRET_KEY = 'thisisasecret'
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.db'
CSRF_ENABLED = True
USER_ENABLE_EMAIL = False


