class Jugador:
    def __init__(self, clase, ps, fuerza, agilidad, vitalidad, energia, exp, estado, items):
        self.clase = clase
        self.ps = ps
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.vitalidad = vitalidad
        self.energia = energia
        self.exp = exp
        self.estado = estado
        self.items = items

    def vive(self):
        return self.ps > 0          #retornará True o False

    def sube_nivel(self):
        self.fuerza     += 5
        self.agilidad   += 5
        self.vitalidad  += 5
        self.energia    += 5


class Enemigo:
    def __init__(self, nombre, ps, fuerza, agilidad, vitalidad, energia, exp):
        self.nombre = str(nombre)
        self.ps = ps
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.vitalidad = vitalidad
        self.energia = energia
        self.exp = exp

    def vive(self):
        return self.ps > 0


class Item:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion




