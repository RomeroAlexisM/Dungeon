import api
from api.app import Session, db
from api.models import Entity


class EntityRepository():

    def get_first(self):
        session = Session()
        session.query(Entity).first()

    def get_all(self):
        session = Session()
        return session.query(Entity).all()

    def get_attributes(self, playable_id):
        print(playable_id)
        session = Session()

        for hp, mana, strength, agility, vitality, energy in session.query(Entity.hp, Entity.mana, Entity.strength,
                                                                           Entity.agility, Entity.vitality,
                                                                           Entity.energy).filter_by(id=playable_id):
            attributes = api.models.Attribute(hp, mana, strength, agility, vitality, energy)
            print(hp, mana, strength, agility, vitality, energy)

        return attributes
