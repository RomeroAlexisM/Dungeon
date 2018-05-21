from core.src.Persistance.EnemyRepository import *

enemiesrepository = EnemyRepository()


class EnemyService():

    def getFirst(self):
        return enemiesrepository.getFirst()

    def getAll(self):
        return enemiesrepository.getAll()