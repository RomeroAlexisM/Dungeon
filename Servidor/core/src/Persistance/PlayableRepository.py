from api.app import db
from api.models import Playable


class PlayableRepository():
    def getFirst(self):
        return Playable.query.first()

    def getAll(self):
        return Playable.query.all()