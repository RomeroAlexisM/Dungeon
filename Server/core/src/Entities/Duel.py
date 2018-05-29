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
            self.player.attacks = True

        else:
            self.opponent.attacks = True

    def turn(self):
        if self.player.attacks:
            self.player.attack(self.opponent, self.player.choose_attack())

            if self.opponent.is_alive():
                self.player.attacks = False
                self.opponent.attacks = True

            else:
                self.player.attacks = False
                self.end_duel()

        else:
            self.opponent.attack(self.player, self.opponent.choose_attack())

            if self.player.is_alive():
                self.opponent.attacks = False
                self.player.attacks = True

            else:
                self.opponent.attacks = False
                self.end_duel()

    def end_duel(self):
        self.finished = True

        print('El duelo ha finished')  # Borrar esto después de testear
