from Servidor.ataques import *
from Servidor.clases import Entidad

MODIFICADOR_DANIO_BASICO = .15
MODIFICADOR_DANIO_ESPECIAL = .30
PUNTOS_NUEVO_NIVEL = 5
VALOR_REGENERACION_VIDA = .2
VALOR_REGENERACION_MANA = .24
CERO = 0


MENSAJE_FALTA_MANA = 'No tienes suficiente mana'


class Guerrero(Entidad):
    def __init__(self):
        super().__init__(clase="Guerrero",
                         ps=20,
                         mana=15,
                         fuerza=30,
                         agilidad=10,
                         vitalidad=20,
                         energia=10,
                         exp=0,
                         items=[],
                         ataques=(Golpear, Ensartada))

    def atacar(self, enemigo, ataque, modificador):

        if ataque.especial:

            if self.suficiente_mana(ataque.costoMana):
                enemigo.ps -= ataque.calcular_danio(MODIFICADOR_DANIO_ESPECIAL, self.fuerza)
                self.perder_mana(ataque.costoMana)

            else:
                print(MENSAJE_FALTA_MANA)

        else:
            enemigo.ps -= ataque.calcular_danio(MODIFICADOR_DANIO_BASICO, self.fuerza)

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


class Mago(Entidad):
    def __init__(self):
        super().__init__(clase="Mago",
                         ps=20,
                         mana=30,
                         fuerza=15,
                         agilidad=10,
                         vitalidad=20,
                         energia=30,
                         exp=0,
                         items=[],
                         ataques=(Fireball, LightingStorm))

    def atacar(self, enemigo, ataque, modificador):

        if ataque.especial:

            if self.suficiente_mana(ataque.costoMana):
                enemigo.ps -= ataque.calcular_danio(MODIFICADOR_DANIO_ESPECIAL, self.energia)
                self.perder_mana(ataque.costoMana)

            else:
                print(MENSAJE_FALTA_MANA)

        else:
            enemigo.ps -= ataque.calcular_danio(MODIFICADOR_DANIO_BASICO, self.energia)

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