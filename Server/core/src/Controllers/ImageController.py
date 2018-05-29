import sys
from flask import jsonify
from api.app import app
from Server.core.src.Services.ImageService import *
sys.path.insert(0, '/home/stalker/PycharmProjects/Dungeon')

imageService = ImageService()


@app.route('/images/character-selection/', methods=['GET'])
def character_selection():
    characters = imageService.getCharacterSelectionImages()
    return jsonify(character_list=[i.serialize for i in characters])

