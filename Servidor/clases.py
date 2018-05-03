class Jugador:
    def __init__(self, clase, ps, mana, fuerza, agilidad, vitalidad, energia, exp, items=[], ataques=()):
        self.clase = clase
        self.ps = ps
        self.mana = mana
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.vitalidad = vitalidad
        self.energia = energia
        self.exp = exp
        self.items = items
        self.ataques = ataques

    def vive(self):
        return self.ps > 0          # retornará True o False

    def sube_nivel(self):
        self.fuerza += 5
        self.agilidad += 5
        self.vitalidad += 5
        self.energia += 5

    def ataque_comun(self):
        pass

    def ataque_especial(self):
        pass

    def renegerar_vida(self):
        self.ps += int(self.vitalidad * 0.2)
        pass

    def regenerar_mana(self):
        self.mana += int(self.energia * 0.2)
        pass

    def recoger_item(self, item):
        self.items.append(item)


class Enemigo:
    def __init__(self, nombre, ps, fuerza, agilidad, vitalidad, energia, exp, ataques=()):
        self.nombre = str(nombre)
        self.ps = ps
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.vitalidad = vitalidad
        self.energia = energia
        self.exp = exp
        self.ataques = ataques

    def vive(self):
        return self.ps > 0

    def ataque_comun(self, ataque, jugador):
        jugador.ps = jugador.ps = ataque.danioBasico


class Item:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class Ataque:
    def __init__(self, nombre, costoMana, danioBasico):
        self.nombre = nombre
        self.costoMana = costoMana
        self.danioBasico = danioBasico