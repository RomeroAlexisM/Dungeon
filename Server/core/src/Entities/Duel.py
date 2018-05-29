class Duel:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.finished = False

    def start(self):
        self.player_attacks_first()
        while not self.finished:
            self.turn()

    def player_attacks_first(self):
        if self.player.agility >= self.opponent.agility:
            self.player.is_attacking = True

        else:
            self.opponent.is_attacking = True

    def turn(self):
        if self.player.is_attacking:
            self.player.attacks(self.opponent, self.player.choose_attack())

            if self.opponent.is_alive():
                self.player.is_attacking = False
                self.opponent.is_attacking = True

            else:
                self.player.is_attacking = False
                self.end_duel()

        else:
            self.opponent.attacks(self.player, self.opponent.choose_attack())

            if self.player.is_alive():
                self.opponent.is_attacking = False
                self.player.is_attacking = True

            else:
                self.opponent = False
                self.end_duel()

    def end_duel(self):
        self.finished = True

        print('El duelo ha finished')  # Borrar esto después de testear
