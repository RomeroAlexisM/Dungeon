from core.src.Persistance.EntityRepository import *

entities_repository = EntityRepository()


class EntityService():

    def get_first(self):
        return entities_repository.get_first()

    def get_all(self):
        return entities_repository.get_all()

    def get_attributes(self, entity_id):
        return entities_repository.get_attributes(entity_id)
