from Servidor.clases import Ataque


# Ataques del Guerrero


class Golpear(Ataque):
    def __init__(self):
        super().__init__(nombre="Golpear",
                         costoMana=0,
                         especial=False)


class Ensartada(Ataque):
    def __init__(self):
        super().__init__(nombre="Ensartada",
                         costoMana=4,
                         especial=True)

# Ataques del Mago


class Fireball(Ataque):
    def __init__(self):
        super().__init__(nombre="Bola de Fuego",
                         costoMana=0,
                         especial=False)


class LightingStorm(Ataque):
    def __init__(self):
        super().__init__(nombre="Tormenta de rayos",
                         costoMana=8,
                         especial=False)

# Ataques de la Rata


class Mordisco(Ataque):
    def __init__(self):
        super().__init__(nombre="Mordisco",
                         costoMana=0,
                         especial=False)


class Escupitajo(Ataque):
    def __init__(self):
        super().__init__(nombre="Escupitajo",
                         costoMana=0,
                         especial=True)

# Ataques del Orco


class GolpeGarrote(Ataque):
    def __init__(self):
        super().__init__(nombre="Golpe de Garrote",
                         costoMana=0,
                         especial=False)


class RompeCraneos(Ataque):
    def __init__(self):
        super().__init__(nombre="Rompecráneos",
                         costoMana=0,
                         especial=True)

# Ataques del Dragón


class Coletazo(Ataque):
    def __init__(self):
        super().__init__(nombre="Coletazo",
                         costoMana=0,
                         especial=False)


class Llamarada(Ataque):
    def __init__(self):
        super().__init__(nombre="Llamarada",
                         costoMana=0,
                         especial=True)