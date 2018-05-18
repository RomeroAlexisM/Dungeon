import sys

from api.app import app
from Servidor.core.src.Services.EnteService import *

sys.path.insert(0, '/home/stalker/PycharmProjects/Dungeon')

entityService = EnteService()


@app.route('/entities/first')
def first():
    firstentity = entityService.getFirst()
    return '<h1>El primer ente es: '+firstentity.nombre+'</h1>'
