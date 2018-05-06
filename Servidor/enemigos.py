from Servidor.ataques import *
from Servidor.clases import Entidad, Duelo

rata = Entidad(id='Rata',
               ps=10,
               mana=8,
               fuerza=2,
               agilidad=8,
               vitalidad=10,
               energia=10,
               exp=5,
               items=[],
               ataques=(mordisco, escupitajo))


troll = Entidad(id='Orco',
                ps=30,
                mana=8,
                fuerza=20,
                agilidad=14,
                vitalidad=30,
                energia=10,
                exp=15,
                items=[],
                ataques=(golpeGarrote, rompeCraneos))


dragon = Entidad(id='Dragon',
                 ps=90,
                 mana=8,
                 fuerza=70,
                 agilidad=30,
                 vitalidad=90,
                 energia=50,
                 exp=5,
                 items=[],
                 ataques=(coletazo, llamarada))

mago = Entidad(id='Mago',
               ps=20,
               mana=30,
               fuerza=15,
               agilidad=10,
               vitalidad=20,
               energia=30,
               exp=0,
               items=[],
               ataques=(fireball, lightingStorm))

duelo = Duelo(mago, rata)
duelo.comenzar_duelo()

