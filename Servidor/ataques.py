from Servidor.clases import Ataque


# Ataques del Guerrero


class Golpear(Ataque):
    def __init__(self):
        super().__init__(nombre="Golpear",
                         costoMana=0,
                         danioBasico=3)

class Ensartada(Ataque):
    def __init__(self):
        super().__init__(nombre="Ensartada",
                         costoMana=4,
                         danioBasico=5)

# Ataques del mago


class Fireball(Ataque):
    def __init__(self):
        super().__init__(nombre="Bola de Fuego",
                         costoMana=0,
                         danioBasico=5)


class LightingStorm(Ataque):
    def __init__(self):
        super().__init__(nombre="Tormenta de rayos",
                         costoMana=8,
                         danioBasico=8)


