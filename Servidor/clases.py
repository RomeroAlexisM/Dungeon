class Jugador:
    def __init__(self, clase, ps, mana, fuerza, agilidad, vitalidad, energia, exp, items, ataques):
        self.clase = clase
        self.ps = ps
        self.mana = mana
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.vitalidad = vitalidad
        self.energia = energia
        self.exp = exp
        self.items = [items]
        self.ataques = (ataques)

    def vive(self):
        return self.ps > 0          # retornará True o False

    def sube_nivel(self):
        self.fuerza += 5
        self.agilidad += 5
        self.vitalidad += 5
        self.energia += 5

    def ataque_debil(self):
        "cambiará dependiendo del personaje"
        pass

    def ataque_fuerte(self):
        pass

    def renegerar_vida(self):
        pass

    def regenerar_mana(self):
        pass


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


class Ataque:
    def __init__(self, nombre, costoMana, danioBasico):
        self.nombre = nombre
        self.costoMana = costoMana
        self.danioBasico = danioBasico