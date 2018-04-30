from Servidor.clases import Jugador


class Guerrero(Jugador):
    def __init__(self):
        super().__init__(clase="Guerrero",
                         ps=20,
                         fuerza=15,
                         agilidad=10,
                         vitalidad=20,
                         energia=10,
                         exp=0,
                         estado="sano",
                         items=[])


class Mago(Jugador):
    def __init__(self):
        super().__init__(clase="Mago",
                         ps=20,
                         fuerza=15,
                         agilidad=10,
                         vitalidad=20,
                         energia=10,
                         exp=0,
                         estado="sano",
                         items=[])