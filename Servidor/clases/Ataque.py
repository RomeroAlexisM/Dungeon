class Ataque:
    def __init__(self, nombre, costomana, especial, multiplicador):
        self.nombre = str(nombre)
        self.costomana = int(costomana)
        self.especial = bool(especial)
        self.multiplicador = str(multiplicador)
