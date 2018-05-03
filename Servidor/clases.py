


class Entidad:
    def __init__(self, ps, mana, fuerza, agilidad, vitalidad, energia, exp, ataques):
        self.ps = ps
        self.mana = mana
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.vitalidad = vitalidad
        self.energia = energia
        self.exp = exp
        self.ataques = ataques

    def vive(self):
        return self.ps > 0

    def atacar(self):
        pass




class Item:
    def __init__(self, nombre, descripcion, equipado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.equipado = equipado

    def equipar(self):
        self.equipado = True

    def desequipar(self):
        self.equipado = False


class Ataque:
    def __init__(self, nombre, costoMana, especial):
        self.nombre = nombre
        self.costoMana = costoMana
        self.especial = especial

    def calcular_danio(self, modificador, atributobase):
        return modificador * atributobase




