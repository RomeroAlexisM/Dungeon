from Servidor.core.src.Entidades.globals import MENSAJE_FALTA_MANA, MODIFICADOR_DANIO_BASICO, STRENGTH, ENERGY, \
    agility, VALOR_REGENERACION_MANA, VALOR_REGENERACION_VIDA, VITALITY, CERO


class Entity:

    def __init__(self, name, level, hp, mana, strength, agility, vitality, energy, defensafisica, defensamagica, estado, exp, items, ataques):
        self.name = str(name)
        self.level = int(level)
        self.hp = int(hp)
        self.mana = int(mana)
        self.strength = int(strength)
        self.agility = int(agility)
        self.vitality = int(vitality)
        self.energy = int(energy)
        self.defensafisica = int(defensafisica)
        self.defensamagica = int(defensamagica)
        self.estado = str(estado)
        self.exp = int(exp)
        self.items = items
        self.ataques = ataques
        self.ataca = False

    def atacar(self, oponente, ataque):
        if ataque.especial:
            if self.suficiente_mana(ataque.costomana):
                from Servidor.core.src.Entidades.globals import MODIFICADOR_DANIO_ESPECIAL
                oponente.hp -= self.calcular_multiplicador(ataque, MODIFICADOR_DANIO_ESPECIAL)
                self.perder_mana(ataque.costomana)
            else:
                print(MENSAJE_FALTA_MANA)

        else:
            oponente.hp -= self.calcular_multiplicador(ataque, MODIFICADOR_DANIO_BASICO)

    def calcular_multiplicador(self, ataque, modificador):
        if ataque.multiplicador == strength:
            return int(self.strength * modificador)

        elif ataque.multiplicador == ENERGY:
            return int(self.energy * modificador)

        elif ataque.multiplicador == agility:
            return int(self.agility * modificador)

        elif ataque.multiplicador == vitality:
            return int(self.vitality * modificador)

    def renegerar_vida(self):
        hp = int(self.vitality * VALOR_REGENERACION_VIDA)
        if self.vitality + hp >= self.vitality:
            self.hp = self.vitality

        else:
            self.hp += hp

    def regenerar_mana(self):
        self.mana += int(self.energy * VALOR_REGENERACION_MANA)

    def perder_mana(self, costomana):
        self.mana -= costomana

    def suficiente_mana(self, costomana):
        return self.mana >= costomana

    def vive(self):

        if self.hp > CERO:
            print("Vida del", self.identificador, " es :", self.hp)
            return True

        else:
            self.hp = CERO
            print("Vida del", self.identificador, " es :", self.hp)
            return False

    def recoger(self, item):
        self.items.append(item)

    def soltar(self, item):
        self.items.pop(item)