from Server.core.src.Entities.Entity import Entity
from Server.core.src.Entities.globals import levels, NEW_LEVEL_POINTS, ONE, TEN, ZERO


class Player(Entity):

    def choose_attack(self):
        attack = self.attack_list[1]
        return attack  # Definir en el futuro como se elige

    def gain_exp(self, enemy):
        level_difference = enemy.level - self.level
        enemy_exp = enemy.exp

        exp_obtained = self.calculate_exp(level_difference, enemy_exp, enemy.level)

        self.level_up(exp_obtained)

    def calculate_exp(self, level_difference, base_exp, enemy_level):
        if level_difference == ZERO:
            return int(base_exp * .8)

        elif level_difference < 0 or level_difference > TEN:
            return int(base_exp * 0.15)

        elif ZERO < level_difference <= TEN:
            percentage = self.level / enemy_level

            return int(base_exp * percentage)

    def level_up(self, exp_obtained):
        actual_exp = self.exp
        actual_level = self.level

        #  Si la experiencia conseguida no supera a la experiencia máxima del level, no sube

        if levels[actual_level] > (actual_exp + exp_obtained):
            self.exp += exp_obtained
            print(self.exp)
            print(actual_exp)
            print(exp_obtained)

        #  recorro la lista desde el level actual hasta el final,
        #  si la experiencia total es mayor significa que pasa de level,
        #  se sube level automáticamente cuando detecta que supera el valor necesario
        #  para pasar de level
        else:
            for item in [key for key in levels if key in range(self.level, len(levels))]:
                if (actual_exp + exp_obtained) >= levels[item]:
                    print(actual_exp + exp_obtained)
                    self.new_level()
                    print('subio al level:', self.level)
                    print('VIT:', self.vitality, 'STR: ', self.strength, 'AGI: ', self.agility, 'ENE: ', self.energy)

            self.exp += exp_obtained
            print('actual_exp', self.exp)

        self.exp += exp_obtained

    def new_level(self):
        self.level += ONE
        self.strength += NEW_LEVEL_POINTS
        self.agility += NEW_LEVEL_POINTS
        self.vitality += NEW_LEVEL_POINTS
        self.energy += NEW_LEVEL_POINTS
