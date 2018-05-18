from core.src.Persistance.EntitiesRepository import *

entitiesRepository = EntitiesRepository()


class EnteService():
    def getFirst(self):
        return entitiesRepository.getFirst()
