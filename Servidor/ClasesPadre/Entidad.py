from Servidor.globales import *


class Entidad:

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

    def atacar(self, enemigo, ataque):
        if ataque.especial:
            if self.suficiente_mana(ataque.costomana):
                enemigo.ps -= self.calcular_multiplicador(ataque, MODIFICADOR_DANIO_ESPECIAL)
                self.perder_mana(ataque.costomana)
            else:
                print(MENSAJE_FALTA_MANA)

        else:
            enemigo.ps -= self.calcular_multiplicador(ataque, MODIFICADOR_DANIO_BASICO)

    def elegir_ataque(self):
        ataque = self.ataques[1]
        return ataque  # Definir en el futuro como se elige

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

    def obtener_experiencia(self, enemigo):
        diferencianivel = enemigo.nivel - self.nivel
        expenemigo = enemigo.exp

        expobtenida = self.calcular_experiencia(diferencianivel, expenemigo, enemigo.nivel)

        self.sube_nivel(expobtenida)

    def calcular_experiencia(self, diferencianivel, expbase, nivelenemigo):
        if diferencianivel == CERO:
            return int(expbase * .8)

        elif diferencianivel < 0 or diferencianivel > DIEZ:
            return int(expbase * 0.15)

        elif CERO < diferencianivel <= DIEZ:
            porcentaje = self.nivel / nivelenemigo

            return int(expbase * porcentaje)

    def sube_nivel(self, expobtenida):
        expactual = self.exp
        nivelactual = self.nivel

        #  Si la experiencia conseguida no supera a la experiencia máxima del nivel, no sube

        if niveles[nivelactual] > (expactual + expobtenida):
            self.exp += expobtenida
            print(self.exp)
            print(expactual)
            print(expobtenida)

        #  recorro la lista desde el nivel actual hasta el final,
        #  si la experiencia total es mayor significa que pasa de nivel,
        #  se sube nivel automáticamente cuando detecta que supera el valor necesario
        #  para pasar de nivel
        else:
            for item in [key for key in niveles if key in range(self.nivel, len(niveles))]:
                if (expactual + expobtenida) >= niveles[item]:
                    print(expactual + expobtenida)
                    self.nuevo_nivel()
                    print('subio al nivel:', self.nivel)
                    print('VIT:', self.vitalidad, 'STR: ', self.fuerza, 'AGI: ', self.agilidad, 'ENE: ', self.energia)

            self.exp += expobtenida
            print('expactual', self.exp)

        self.exp += expobtenida

    def nuevo_nivel(self):
        self.nivel += UNO
        self.fuerza += PUNTOS_NUEVO_NIVEL
        self.agilidad += PUNTOS_NUEVO_NIVEL
        self.vitalidad += PUNTOS_NUEVO_NIVEL
        self.energia += PUNTOS_NUEVO_NIVEL

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
