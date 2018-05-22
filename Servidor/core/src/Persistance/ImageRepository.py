from api.app import db
from api.models import Image


class ImageRepository():

    def getAllCharacters(self):
        return Image.query.all()