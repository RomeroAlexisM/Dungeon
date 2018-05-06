MODIFICADOR_DANIO_BASICO = .15
MODIFICADOR_DANIO_ESPECIAL = .30
PUNTOS_NUEVO_NIVEL = 5
VALOR_REGENERACION_VIDA = .2
VALOR_REGENERACION_MANA = .24
CERO = 0
FUERZA = 'Fuerza'
ENERGIA = 'Energia'
AGILIDAD = 'Agilidad'
VITALIDAD = 'Vitalidad'

MENSAJE_FALTA_MANA = 'No tienes suficiente mana'


class Entidad:

    def __init__(self, id, ps, mana, fuerza, agilidad, vitalidad, energia, exp, items, ataques):
        self.id = str(id)
        self.ps = ps
        self.mana = int(mana)
        self.fuerza = int(fuerza)
        self.agilidad = int(agilidad)
        self.vitalidad = int(vitalidad) # el valor de la vitalidad será lo máximo de vida que tendrá la barra
        self.energia = int(energia)
        self.exp = int(exp)
        self.items = items
        self.ataques = ataques
        self.ataca = False


    def atacar(self, enemigo, ataque):

        if ataque.especial:

            if self.suficiente_mana(ataque.costoMana):
                enemigo.ps -= self.calcular_multiplicador(ataque, MODIFICADOR_DANIO_ESPECIAL)
                self.perder_mana(ataque.costoMana)

            else:
                print(MENSAJE_FALTA_MANA)

        else:
            enemigo.ps -= ataque.calcular_multiplicador(ataque, MODIFICADOR_DANIO_BASICO)

    def elegir_ataque(self):
        ataque = Ataque
        return ataque # Definir en el futuro como se elige

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

    def perder_mana(self, mana):
        self.mana -= mana

    def nuevo_nivel(self):
        self.fuerza += PUNTOS_NUEVO_NIVEL
        self.agilidad += PUNTOS_NUEVO_NIVEL
        self.vitalidad += PUNTOS_NUEVO_NIVEL
        self.energia += PUNTOS_NUEVO_NIVEL

    def suficiente_mana(self, costomana):
        return self.mana >= costomana

    def vive(self):
        return self.ps > 0


class Item:
    def __init__(self, nombre, descripcion, equipado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.equipado = equipado

    def equipar(self):
        self.equipado = True

    def desequipar(self):
        self.equipado = False


class Ataque:
    def __init__(self, nombre, costoMana, especial, multiplicador):
        self.nombre = str(nombre)
        self.costoMana = int(costoMana)
        self.especial = bool(especial)
        self.multiplicador = str(multiplicador)

class Duelo:
    def __init__(self, jugador, oponente):
        self.jugador = Entidad(jugador)
        self.oponente = Entidad(oponente)
        self.finalizado = False

    def jugador_ataca_primero(self):
        if self.jugador.agilidad >= self.oponente.agilidad:
            self.jugador.ataca = True

        else:
            self.oponente.ataca = True

    def comenzar_duelo(self):
        self.jugador_ataca_primero()
        while not self.finalizado:
            self.turno()

    def finalizar_duelo(self):
        self.finalizado = True
        print('El duelo ha finalizado')  # Borrar esto después de testear

    def turno(self):
        if self.jugador.ataca:
            self.jugador.atacar(self.oponente, self.jugador.elegir_ataque())

            if self.oponente.vive():
                self.jugador.ataca = False
                self.oponente.ataca = True

            else:
                self.jugador.ataca = False
                self.finalizar_duelo()

        else:
            self.oponente.atacar(self.jugador, self.oponente.elegir_ataque())

            if self.jugador.vive():
                self.oponente.ataca = False
                self.jugador.ataca = True

            else:
                self.oponente.ataca = False
                self.finalizar_duelo()










