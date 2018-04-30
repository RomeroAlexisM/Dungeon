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
                         ps=10,
                         fuerza=2,
                         agilidad=8,
                         vitalidad=6,
                         energia=10,
                         exp=5)


class Dragon(Enemigo):
    def __init__(self):
        super().__init__(name="Dragon",
                         ps=10,
                         fuerza=2,
                         agilidad=8,
                         vitalidad=6,
                         energia=10,
                         exp=5)