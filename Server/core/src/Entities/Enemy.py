import random
from Servidor.core.src.Entidades.Ente import Ente
from Servidor.core.src.Entidades.globals import MODIFICADOR_DANIO_ESPECIAL, MODIFICADOR_DANIO_BASICO


class Enemy(Entity):

    def atacar(self, oponente, ataque):
        if ataque.especial:
            oponente.ps -= self.calcular_multiplicador(ataque, MODIFICADOR_DANIO_ESPECIAL)
            self.perder_mana(ataque.costomana)

        else:
            oponente.ps -= self.calcular_multiplicador(ataque, MODIFICADOR_DANIO_BASICO)

    def elegir_ataque(self):
        ataquealeatorio = random.choice(self.ataques)

        while not self.suficiente_mana(ataquealeatorio.costomana):
            ataquealeatorio = random.choice(self.ataques)

        return ataquealeatorio
