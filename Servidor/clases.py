MODIFICADOR_DANIO_BASICO = .15
MODIFICADOR_DANIO_ESPECIAL = .30
PUNTOS_NUEVO_NIVEL = 5
VALOR_REGENERACION_VIDA = .2
VALOR_REGENERACION_MANA = .24
CERO = 0

MENSAJE_FALTA_MANA = 'No tienes suficiente mana'


class Entidad:
    def __init__(self, id, ps, mana, fuerza, agilidad, vitalidad, energia, exp, ataques):
        self.id = str(id)
        self.ps = int(ps)
        self.mana = int(mana)
        self.fuerza = int(fuerza)
        self.agilidad = int(agilidad)
        self.vitalidad = int(vitalidad)
        self.energia = int(energia)
        self.exp = int(exp)
        self.ataques = ataques
        self.atributobase = CERO

    def set_atributobase(self, atributobase):
        self.atributobase = atributobase

    def atacar(self, enemigo, ataque, atributobase):

        if ataque.especial:

            if self.suficiente_mana(ataque.costoMana):
                enemigo.ps -= ataque.calcular_danio(MODIFICADOR_DANIO_ESPECIAL, atributobase)
                self.perder_mana(ataque.costoMana)

            else:
                print(MENSAJE_FALTA_MANA)

        else:
            enemigo.ps -= ataque.calcular_danio(MODIFICADOR_DANIO_BASICO, atributobase)

    def renegerar_vida(self):
        self.ps += int(self.vitalidad * VALOR_REGENERACION_VIDA)

    def regenerar_mana(self):
        self.mana += int(self.energia * VALOR_REGENERACION_MANA)

    def perder_mana(self, mana):
        self.mana -= mana

    def nuevo_nivel(self):
        self.fuerza += PUNTOS_NUEVO_NIVEL
        self.agilidad += PUNTOS_NUEVO_NIVEL
        self.vitalidad += PUNTOS_NUEVO_NIVEL
        self.energia += PUNTOS_NUEVO_NIVEL

    def suficiente_mana(self, costomana):
        return self.mana >= costomana

    def vive(self):
        return self.ps > 0

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



