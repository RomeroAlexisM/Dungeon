class Attack:
    def __init__(self, name, manacost, special, multiplier):
        self.name = str(name)
        self.mana_cost = int(manacost)
        self.special = bool(special)
        self.multiplier = str(multiplier)
