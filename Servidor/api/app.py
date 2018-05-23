from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from core.src.Controllers.EntidadController import *
from core.src.Controllers.EnemyController import *
from core.src.Controllers.ImageController import *
from core.src.Controllers.UserController import *

db.create_all()
if __name__ == '__main__':
    app.run()
