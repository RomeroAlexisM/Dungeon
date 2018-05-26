from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, SQLAlchemyAdapter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
from core.src.Controllers.EntidadController import *
from core.src.Controllers.EnemyController import *
from core.src.Controllers.ImageController import *
from core.src.Controllers.UserController import *

if __name__ == '__main__':
    app.run()
