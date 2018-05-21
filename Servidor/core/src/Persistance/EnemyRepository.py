from api.app import db
from api.models import Enemy


class EnemyRepository():

    def getFirst(self):
        return Enemy.query.first()

    def getAll(self):
        return Enemy.query.all()
