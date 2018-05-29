from Server.core.src.Entities.Duel import Duel
from Server.core.src.Entities.Enemy import Enemy
from Server.core.src.Entities.Player import Player
from Server.core.src.Persistance.attacks import *

rata = Enemy(name='Rata',
             level=2,
             hp=10,
             mana=8,
             strength=2,
             agility=8,
             vitality=10,
             energy=10,
             physical_defense=0,
             magical_defense=0,
             status='',
             exp=5,
             items=[],
             attack_list=(mordisco, escupitajo))

troll = Enemy(name='Troll',
              level=20,
              hp=30,
              mana=8,
              strength=20,
              agility=14,
              vitality=30,
              energy=10,
              physical_defense=0,
              magical_defense=0,
              status='',
              exp=5000,
              items=[],
              attack_list=(golpeGarrote, rompeCraneos))


dragon = Enemy(name='Dragon',
               level=40,
               hp=90,
               mana=8,
               strength=70,
               agility=30,
               vitality=90,
               energy=50,
               physical_defense=0,
               magical_defense=0,
               status='',
               exp=5,
               items=[],
               attack_list=(coletazo, llamarada))

#  ESTE MAGO ES PARA TESTEAR (LUEGO SE IMPLEMENTARAN TEST UNITARIOS)

mago = Player(name='Mago',
              level=1,
              hp=20,
              mana=30,
              strength=15,
              agility=10,
              vitality=20,
              energy=30,
              physical_defense=0,
              magical_defense=0,
              status='',
              exp=0,
              items=[],
              attack_list=(fireball, lightingStorm))


duel = Duel(mago, troll)
duel.start()
mago.gain_exp(troll)
