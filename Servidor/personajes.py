from Servidor.ataques import *
from Servidor.ClasesPadre.Entidad import Entidad

guerrero = Entidad(identificador='Guerrero',
                   nivel=1,
                   ps=20,
                   mana=15,
                   fuerza=30,
                   agilidad=10,
                   vitalidad=20,
                   energia=10,
                   exp=0,
                   items=[],
                   ataques=(golpear, ensartada))

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
