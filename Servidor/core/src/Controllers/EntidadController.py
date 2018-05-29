import sys
from flask import jsonify, request, json
from api.app import app
from Servidor.core.src.Services.PlayableService import *
sys.path.insert(0, '/home/stalker/PycharmProjects/Dungeon')

entity_service = EntityService()


@app.route('/playable/first/', methods=['GET'])
def get_first():
    first_entity = entity_service.get_first()
    return '<h1>El primer ente es: '+first_entity.nombre+'</h1>'


@app.route('/playable/all/', methods=['GET'])
def get_entities():
    entities = entity_service.get_all()
    return jsonify(playables_list=[i.serialize for i in entities])


@app.route('/playable/attributes/<playable_id>', methods=['GET'])
def get_attributes(entity_id):
    attributes = entity_service.get_attributes(entity_id)
    return json.dumps(attributes.__dict__)

