from Servidor.ClasesPadre.Item import Item


class Equipable(Item):

    def equipar(self):
        self.equipado = True

    def desequipar(self):
        self.equipado = False