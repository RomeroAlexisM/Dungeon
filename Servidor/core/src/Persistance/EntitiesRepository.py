from api.app import db
from api.models import Ente


class EntitiesRepository():
    def getFirst(self):
        # db.create_all()
        return Ente.query.first()