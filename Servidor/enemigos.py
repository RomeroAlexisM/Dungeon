from Servidor.ataques import *
from Servidor.clases import Enemigo


class Rata(Enemigo):
    def __init__(self):
        super().__init__(name="Rata",
                         ps=10,
                         fuerza=2,
                         agilidad=8,
                         vitalidad=6,
                         energia=10,
                         exp=5,
                         ataques=(Mordisco, Escupitajo))


class Troll(Enemigo):
    def __init__(self):
        super().__init__(name="Orco",
                         ps=25,
                         fuerza=20,
                         agilidad=14,
                         vitalidad=30,
                         energia=10,
                         exp=15,
                         ataques=(GolpeGarrote, RompeCraneos))


class Dragon(Enemigo):
    def __init__(self):
        super().__init__(name="Dragon",
                         ps=45,
                         fuerza=70,
                         agilidad=30,
                         vitalidad=90,
                         energia=50,
                         exp=5,
                         ataques=(Coletazo, Llamarada))