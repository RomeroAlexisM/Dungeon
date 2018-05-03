from Servidor.ataques import *
from Servidor.clases import Entidad


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

    def ataque_comun(self, ataque, enemigo):

        enemigo.ps = enemigo.ps - ataque.danioBasico

    def ataque_especial(self, ataque, enemigo):

        if ataque.costoMana <= self.mana:
            danioAtaque = (self.fuerza * 0.6) + ataque.danioBasico
            self.mana -= ataque.costoMana
            enemigo.ps = enemigo.ps - danioAtaque
        else:
            print("No tienes suficiente mana")


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