from core.src.Persistance.ImageRepository import *

imagesRepository = ImageRepository()


class ImageService():

    def getCharacterSelectionImages(self):
        return imagesRepository.getAllCharacters()
