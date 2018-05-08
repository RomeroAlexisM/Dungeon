from Servidor.ataques import *
from Servidor.clases.Entidad import Entidad

rata = Entidad(identificador='Rata',
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


troll = Entidad(identificador='Troll',
                nivel=20,
                ps=30,
                mana=8,
                fuerza=20,
                agilidad=14,
                vitalidad=30,
                energia=10,
                exp=5000,
                items=[],
                ataques=(golpeGarrote, rompeCraneos))


dragon = Entidad(identificador='Dragon',
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

mago = Entidad(identificador='Mago',
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

#  duelo = Duelo(mago, troll)
#  duelo.comenzar_duelo()
#  mago.obtener_experiencia(troll)
