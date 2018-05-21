from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from core.src.Controllers.EntidadController import *
from core.src.Controllers.EnemyController import *

if __name__ == '__main__':
    app.run()
