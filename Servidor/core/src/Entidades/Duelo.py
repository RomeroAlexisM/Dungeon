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
