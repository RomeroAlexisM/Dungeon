from Server.core.src.Entities.Entity import Entity
from core.src.Persistance.attacks import *

guerrero = Entity(name='Guerrero',
                  level=1,
                  hp=20,
                  mana=15,
                  strength=30,
                  agility=10,
                  vitality=20,
                  energy=10,
                  physical_defense=0,
                  magical_defense=0,
                  status='',
                  exp=0,
                  items=[],
                  attack_list=(golpear, ensartada))

mago = Entity(name='Mago',
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
