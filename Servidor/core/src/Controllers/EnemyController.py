import sys
from flask import jsonify
from api.app import app
from Servidor.core.src.Services.EnemyService import *
sys.path.insert(0, '/home/stalker/PycharmProjects/Dungeon')

enemyService = EnemyService()


@app.route('/enemies/first/', methods=['GET'])
def first_enemy():
    firstenemy = enemyService.getFirst()
    return '<h1>El primer ente es: ' + firstenemy.nombre + '</h1>'


@app.route('/enemies/all/', methods=['GET'])
def all_enemies():
    enemies = enemyService.getAll()
    return jsonify(json_list=[i.serialize for i in enemies])
