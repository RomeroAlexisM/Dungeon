# -*- coding: utf-8 -*-
import sys
from flask import jsonify
from api.app import app
sys.path.insert(0, '/home/stalker/PycharmProjects/Dungeon')
from flask_user import login_required

@app.route('/')
def index():
    return '<h1>Página principal</h1>'


@app.route('/profile')
@login_required
def profile():
    return '<h1>Esto es una página de perfiles prtoegida</h1>'
