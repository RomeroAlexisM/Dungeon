from Servidor.clases import Ataque

FUERZA = 'Fuerza'
ENERGIA = 'Energia'
AGILIDAD = 'Agilidad'
VITALIDAD = 'Vitalidad'


# Ataques del Guerrero


golpear = Ataque(nombre="Golpear",
                 costoMana=0,
                 especial=False,
                 multiplicador=FUERZA)


ensartada = Ataque(nombre="Ensartada",
                   costoMana=4,
                   especial=True,
                   multiplicador=FUERZA)

# Ataques del Mago


fireball = Ataque(nombre="Bola de Fuego",
                  costoMana=0,
                  especial=False,
                  multiplicador=ENERGIA)


lightingStorm = Ataque(nombre="Tormenta de rayos",
                       costoMana=8,
                       especial=True,
                       multiplicador=ENERGIA)

# Ataques de la Rata


mordisco = Ataque(nombre="Mordisco",
                  costoMana=0,
                  especial=False,
                  multiplicador=AGILIDAD)


escupitajo = Ataque(nombre="Escupitajo",
                    costoMana=0,
                    especial=True,
                    multiplicador=AGILIDAD)

# Ataques del Orco


golpeGarrote = Ataque(nombre="Golpe de Garrote",
                      costoMana=0,
                      especial=False,
                      multiplicador=FUERZA)


rompeCraneos = Ataque(nombre="Rompecráneos",
                      costoMana=0,
                      especial=True,
                      multiplicador=FUERZA)

# Ataques del Dragón


coletazo = Ataque(nombre="Coletazo",
                  costoMana=0,
                  especial=False,
                  multiplicador=VITALIDAD)


llamarada = Ataque(nombre="Llamarada",
                   costoMana=0,
                   especial=True,
                   multiplicador=ENERGIA)