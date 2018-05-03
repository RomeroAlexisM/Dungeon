CINCO = 5
VALOR_REGENERACION_VIDA = .2
VALOR_REGENERACION_MANA = .2


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

    def sube_nivel(self):
        self.fuerza += CINCO
        self.agilidad += CINCO
        self.vitalidad += CINCO
        self.energia += CINCO

    def atacar(self):
        pass

    def renegerar_vida(self):
        self.ps += int(self.vitalidad * VALOR_REGENERACION_VIDA)

    def regenerar_mana(self):
        self.mana += int(self.energia * VALOR_REGENERACION_MANA)

    def recoger_item(self, item):
        self.items.append(item)


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