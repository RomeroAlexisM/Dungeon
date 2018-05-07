MODIFICADOR_DANIO_BASICO = .15
MODIFICADOR_DANIO_ESPECIAL = .30
PUNTOS_NUEVO_NIVEL = 5
VALOR_REGENERACION_VIDA = .02
VALOR_REGENERACION_MANA = .02
CERO = 0
UNO = 1
DIEZ = 10
FUERZA = 'Fuerza'
ENERGIA = 'Energia'
AGILIDAD = 'Agilidad'
VITALIDAD = 'Vitalidad'

MENSAJE_FALTA_MANA = 'No tienes suficiente mana'

NIVELES = ((0, 0),
           (1, 50), (2, 100), (3, 200), (4, 400), (5, 750),
           (6, 1300), (7, 2100), (8, 3100), (9, 4650), (10, 4650),
           (11, 6500), (12, 8800), (13, 11600), (14, 14950), (15, 18900),
           (16, 23500), (17, 28800), (18, 34850), (19, 41700), (20, 49400))


class Entidad:

    def __init__(self, id, nivel, ps, mana, fuerza, agilidad, vitalidad, energia, exp, items, ataques):
        self.id = str(id)
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
        experienciabaseenemigo = enemigo.exp

        expobtenida = self.calcular_experiencia(diferencianivel, experienciabaseenemigo, enemigo.nivel)

    def calcular_experiencia(self, diferencianivel, experienciabase, nivelenemigo):
        if diferencianivel == CERO:
            return int(experienciabase * .8)

        elif diferencianivel < 0 or diferencianivel >DIEZ:
            return int(experienciabase * 0.15)

        elif diferencianivel > CERO and diferencianivel <= DIEZ:
            porcentaje = self.nivel / nivelenemigo

            return int(experienciabase * porcentaje)




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
            print("Vida del", self.id, " es :", self.ps)
            return True

        else:
            self.ps = CERO
            print("Vida del", self.id, " es :", self.ps)
            return False


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
    def __init__(self, nombre, costomana, especial, multiplicador):
        self.nombre = str(nombre)
        self.costomana = int(costomana)
        self.especial = bool(especial)
        self.multiplicador = str(multiplicador)


class Duelo:
    def __init__(self, jugador, oponente):
        self.jugador = jugador
        self.oponente = oponente
        self.finalizado = False

    def comenzar_duelo(self):
        self.jugador_ataca_primero()
        while not self.finalizado:
            self.turno()

    def jugador_ataca_primero(self):
        if self.jugador.agilidad >= self.oponente.agilidad:
            self.jugador.ataca = True

        else:
            self.oponente.ataca = True

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

    def finalizar_duelo(self):
        self.finalizado = True

        print('El duelo ha finalizado')  # Borrar esto después de testear
