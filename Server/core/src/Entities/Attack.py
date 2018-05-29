class Attack:
    def __init__(self, name, mana_cost, special, multiplier):
        self.name = str(name)
        self.mana_cost = int(mana_cost)
        self.special = bool(special)
        self.multiplier = str(multiplier)
