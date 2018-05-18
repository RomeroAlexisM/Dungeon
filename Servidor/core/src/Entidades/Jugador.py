from Servidor.core.src.Entidades.Ente import Ente
from Servidor.core.globales import niveles, PUNTOS_NUEVO_NIVEL, UNO, DIEZ, CERO


class Jugador(Ente):

    def elegir_ataque(self):
        ataque = self.ataques[1]
        return ataque  # Definir en el futuro como se elige

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
