import random
from Server.core.src.Entities.Entity import Entity
from Server.core.src.Entities.globals import SPECIAL_DADMAGE_MODIFIER, BASE_DADMAGE_MODIFIER


class Enemy(Entity):

    def attacks(self, opponent, attack):
        if attack.special:
            opponent.hp -= self.calculate_multiplier(attack, SPECIAL_DADMAGE_MODIFIER)
            self.lose_mana(attack.mana_cost)

        else:
            opponent.hp -= self.calculate_multiplier(attack, BASE_DADMAGE_MODIFIER)

    def choose_attack(self):
        random_attack = random.choice(self.attack_list)

        while not self.enough_mana(random_attack.mana_cost):
            random_attack = random.choice(self.attacks)

        return random_attack

