from Servidor.clases import Enemigo


class Rata(Enemigo):
    def __init__(self):
        super().__init__(name="Rata",
                         ps=10,
                         fuerza=2,
                         agilidad=8,
                         vitalidad=6,
                         energia=10,
                         exp=5)


class Troll(Enemigo):
    def __init__(self):
        super().__init__(name="Orco",
                         ps=25,
                         fuerza=10,
                         agilidad=4,
                         vitalidad=30,
                         energia=30,
                         exp=10)


class Dragon(Enemigo):
    def __init__(self):
        super().__init__(name="Dragon",
                         ps=100,
                         fuerza=40,
                         agilidad=30,
                         vitalidad=80,
                         energia=60,
                         exp=40)