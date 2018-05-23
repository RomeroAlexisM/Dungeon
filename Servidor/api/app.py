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


if __name__ == '__main__':
    # user_manager = UserManager()
    # user_manager.init_app(app)
    # login_manager = LoginManager()
    # login_manager.init_app(app)
    # login_manager.login_view = 'login'
    app.run()
