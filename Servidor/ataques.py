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

# Ataques de la rata


class Mordisco(Ataque):
    def __init__(self):
        super().__init__(nombre="Mordisco",
                         costoMana=0,
                         danioBasico=4)


class Escupitajo(Ataque):
    def __init__(self):
        super().__init__(nombre="Escupitajo",
                         costoMana=0,
                         danioBasico=6)

# Ataques del orco


class GolpeGarrote(Ataque):
    def __init__(self):
        super().__init__(nombre="Golpe de Garrote",
                         costoMana=0,
                         danioBasico=8)


class RompeCraneos(Ataque):
    def __init__(self):
        super().__init__(nombre="Rompecráneos",
                         costoMana=0,
                         danioBasico=15)

# Ataques del Dragón


class Coletazo(Ataque):
    def __init__(self):
        super().__init__(nombre="Coletazo",
                         costoMana=0,
                         danioBasico=19)


class Llamarada(Ataque):
    def __init__(self):
        super().__init__(nombre="Llamarada",
                         costoMana=0,
                         danioBasico=23)