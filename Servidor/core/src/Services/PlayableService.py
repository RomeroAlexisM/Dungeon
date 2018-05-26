from core.src.Persistance.PlayableRepository import *

playablesrepository = PlayableRepository()


class PlayableService():

    def getFirst(self):
        return playablesrepository.getFirst()

    def getAll(self):
        return playablesrepository.getAll()

    def get_attributes(self, playable_id):
        return playablesrepository.get_attributes(playable_id)