from Servidor.ataques import *
from Servidor.clases import Entidad

rata = Entidad(id='Rata',
               ps=10,
               fuerza=2,
               agilidad=8,
               vitalidad=6,
               energia=10,
               exp=5,
               ataques=(mordisco, escupitajo))


troll = Entidad(id='Orco',
                ps=25,
                fuerza=20,
                agilidad=14,
                vitalidad=30,
                energia=10,
                exp=15,
                ataques=(golpeGarrote, rompeCraneos))


dragon = Entidad(id='Dragon',
                 ps=45,
                 fuerza=70,
                 agilidad=30,
                 vitalidad=90,
                 energia=50,
                 exp=5,
                 ataques=(coletazo, llamarada))