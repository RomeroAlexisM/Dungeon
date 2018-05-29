from Server.core.src.Entities.Attack import Attack
from Server.core.src.Entities.globals import STRENGTH, ENERGY, AGILITY, VITALITY


#  Ataques del Guerrero

golpear = Attack(name="Golpear",
                 mana_cost=0,
                 special=False,
                 multiplier=STRENGTH)

ensartada = Attack(name="Ensartada",
                   mana_cost=4,
                   special=True,
                   multiplier=STRENGTH)

# Ataques del Mago

fireball = Attack(name="Bola de Fuego",
                  mana_cost=0,
                  special=False,
                  multiplier=ENERGY)

lightingStorm = Attack(name="Tormenta de rayos",
                       mana_cost=8,
                       special=True,
                       multiplier=ENERGY)

# Ataques de la Rata


mordisco = Attack(name="Mordisco",
                  mana_cost=0,
                  special=False,
                  multiplier=AGILITY)

escupitajo = Attack(name="Escupitajo",
                    mana_cost=0,
                    special=True,
                    multiplier=AGILITY)

# Ataques del Orco

golpeGarrote = Attack(name="Golpe de Garrote",
                      mana_cost=0,
                      special=False,
                      multiplier=STRENGTH)

rompeCraneos = Attack(name="Rompecráneos",
                      mana_cost=0,
                      special=True,
                      multiplier=STRENGTH)

# Ataques del Dragón


coletazo = Attack(name="Coletazo",
                  mana_cost=0,
                  special=False,
                  multiplier=VITALITY)

llamarada = Attack(name="Llamarada",
                   mana_cost=0,
                   special=True,
                   multiplier=ENERGY)
