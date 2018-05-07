from Servidor.ataques import *
from Servidor.clases import Entidad, Duelo

rata = Entidad(id='Rata',
               nivel=2,
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
                nivel=5,
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
                 nivel=40,
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
               nivel=1,
               ps=20,
               mana=30,
               fuerza=15,
               agilidad=10,
               vitalidad=20,
               energia=30,
               exp=0,
               items=[],
               ataques=(fireball, lightingStorm))

duelo = Duelo(mago, troll)
duelo.comenzar_duelo()
