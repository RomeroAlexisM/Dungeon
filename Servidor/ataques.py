from Servidor.clases import Ataque

FUERZA = 'Fuerza'
ENERGIA = 'Energia'
AGILIDAD = 'Agilidad'
VITALIDAD = 'Vitalidad'


# Ataques del Guerrero


golpear = Ataque(nombre="Golpear",
                 costomana=0,
                 especial=False,
                 multiplicador=FUERZA)


ensartada = Ataque(nombre="Ensartada",
                   costomana=4,
                   especial=True,
                   multiplicador=FUERZA)

# Ataques del Mago


fireball = Ataque(nombre="Bola de Fuego",
                  costomana=0,
                  especial=False,
                  multiplicador=ENERGIA)


lightingStorm = Ataque(nombre="Tormenta de rayos",
                       costomana=8,
                       especial=True,
                       multiplicador=ENERGIA)

# Ataques de la Rata


mordisco = Ataque(nombre="Mordisco",
                  costomana=0,
                  especial=False,
                  multiplicador=AGILIDAD)


escupitajo = Ataque(nombre="Escupitajo",
                    costomana=0,
                    especial=True,
                    multiplicador=AGILIDAD)

# Ataques del Orco


golpeGarrote = Ataque(nombre="Golpe de Garrote",
                      costomana=0,
                      especial=False,
                      multiplicador=FUERZA)


rompeCraneos = Ataque(nombre="Rompecráneos",
                      costomana=0,
                      especial=True,
                      multiplicador=FUERZA)

# Ataques del Dragón


coletazo = Ataque(nombre="Coletazo",
                  costomana=0,
                  especial=False,
                  multiplicador=VITALIDAD)


llamarada = Ataque(nombre="Llamarada",
                   costomana=0,
                   especial=True,
                   multiplicador=ENERGIA)