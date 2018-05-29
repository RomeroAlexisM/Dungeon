from Server.core.src.Entities.globals import NOT_ENOUGH_MANA_MESSAGE, BASE_DADMAGE_MODIFIER, STRENGTH, ENERGY, \
    AGILITY, MANA_REGENERATION_VALUE, HP_REGENERATION_VALUE, VITALITY, ZERO


class Entity:

    def __init__(self, name, level, hp, mana, strength, agility, vitality, energy, physical_defense, magical_defense,
                 status, exp, items, attack_list):
        self.name = str(name)
        self.level = int(level)
        self.hp = int(hp)
        self.mana = int(mana)
        self.strength = int(strength)
        self.agility = int(agility)
        self.vitality = int(vitality)
        self.energy = int(energy)
        self.physical_defense = int(physical_defense)
        self.magical_defense = int(magical_defense)
        self.status = str(status)
        self.exp = int(exp)
        self.items = items
        self.is_attacking = False
        self.attack_list = attack_list
        self.attack = False

    def attacks(self, opponent, attack):
        if attack.special:
            if self.enough_mana(attack.mana_cost):
                from Server.core.src.Entities.globals import SPECIAL_DADMAGE_MODIFIER
                opponent.hp -= self.calculate_multiplier(attack, SPECIAL_DADMAGE_MODIFIER)
                self.lose_mana(attack.mana_cost)
            else:
                print(NOT_ENOUGH_MANA_MESSAGE)

        else:
            opponent.hp -= self.calculate_multiplier(attack, BASE_DADMAGE_MODIFIER)

    def calculate_multiplier(self, attack, modifier):
        if attack.multiplier == STRENGTH:
            return int(self.strength * modifier)

        elif attack.multiplier == ENERGY:
            return int(self.energy * modifier)

        elif attack.multiplier == AGILITY:
            return int(self.agility * modifier)

        elif attack.multiplier == VITALITY:
            return int(self.vitality * modifier)

    def regenerate_hp(self):
        hp = int(self.vitality * HP_REGENERATION_VALUE)
        if self.vitality + hp >= self.vitality:
            self.hp = self.vitality

        else:
            self.hp += hp

    def regenerate_mana(self):
        self.mana += int(self.energy * MANA_REGENERATION_VALUE)

    def lose_mana(self, mana_cost):
        self.mana -= mana_cost

    def enough_mana(self, mana_cost):
        return self.mana >= mana_cost

    def is_alive(self):

        if self.hp > ZERO:
            print("Vida del", self.name, " es :", self.hp)
            return True

        else:
            self.hp = ZERO
            print("Vida del", self.name, " es :", self.hp)
            return False

    def pick_up(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.pop(item)
