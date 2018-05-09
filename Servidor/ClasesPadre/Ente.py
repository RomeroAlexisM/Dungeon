from Servidor.globales import *


class Ente:

    def __init__(self, identificador, nivel, ps, mana, fuerza, agilidad, vitalidad, energia, exp, items, ataques):
        self.identificador = str(identificador)
        self.nivel = int(nivel)
        self.ps = int(ps)
        self.mana = int(mana)
        self.fuerza = int(fuerza)
        self.agilidad = int(agilidad)
        self.vitalidad = int(vitalidad)  # el valor de la vitalidad será lo máximo de vida que tendrá la barra
        self.energia = int(energia)
        self.exp = int(exp)
        self.items = items
        self.ataques = ataques
        self.ataca = False

    def atacar(self, oponente, ataque):
        if ataque.especial:
            if self.suficiente_mana(ataque.costomana):
                oponente.ps -= self.calcular_multiplicador(ataque, MODIFICADOR_DANIO_ESPECIAL)
                self.perder_mana(ataque.costomana)
            else:
                print(MENSAJE_FALTA_MANA)

        else:
            oponente.ps -= self.calcular_multiplicador(ataque, MODIFICADOR_DANIO_BASICO)

    def calcular_multiplicador(self, ataque, modificador):
        if ataque.multiplicador == FUERZA:
            return int(self.fuerza * modificador)

        elif ataque.multiplicador == ENERGIA:
            return int(self.energia * modificador)

        elif ataque.multiplicador == AGILIDAD:
            return int(self.agilidad * modificador)

        elif ataque.multiplicador == VITALIDAD:
            return int(self.vitalidad * modificador)

    def renegerar_vida(self):
        ps = int(self.vitalidad * VALOR_REGENERACION_VIDA)
        if self.vitalidad + ps >= self.vitalidad:
            self.ps = self.vitalidad

        else:
            self.ps += ps

    def regenerar_mana(self):
        self.mana += int(self.energia * VALOR_REGENERACION_MANA)

    def perder_mana(self, costomana):
        self.mana -= costomana

    def suficiente_mana(self, costomana):
        return self.mana >= costomana

    def vive(self):

        if self.ps > CERO:
            print("Vida del", self.identificador, " es :", self.ps)
            return True

        else:
            self.ps = CERO
            print("Vida del", self.identificador, " es :", self.ps)
            return False

    def recoger(self, item):
        self.items.append(item)

    def soltar(self, item):
        self.items.pop(item)