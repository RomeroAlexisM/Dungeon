import sys
from flask import jsonify
from api.app import app
from Servidor.core.src.Services.PlayableService import *
sys.path.insert(0, '/home/stalker/PycharmProjects/Dungeon')

playableService = PlayableService()


@app.route('/playable/first/', methods=['GET'])
def first():
    firstplayable = playableService.getFirst()
    return '<h1>El primer ente es: '+firstplayable.nombre+'</h1>'


@app.route('/playable/all/', methods=['GET'])
def playables():
    playables = playableService.getAll()
    return jsonify(playables_list=[i.serialize for i in playables])

