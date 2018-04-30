import classes

class Rata(Enemigo):
    def __init__(self):
        super(Rata, self).__init__(name = "Rata",
                                   ps = 10,
                                   fuerza = 2,
                                   agilidad = 8,
                                   vitalidad = 6,
                                   energia = 10,
                                   exp = 5)

class Troll(Enemigo):
    def __init__(self):
        super(Troll, self).__init__(name = "Orco",
                                   ps = 25,
                                   fuerza = 10,
                                   agilidad = 6,
                                   vitalidad = 15,
                                   energia = 30,
                                   exp = 10)

class Dragon(Enemigo):
    def __init__(self):
        super(Dragon, self).__init__(name = "Rata",
                                   ps = 50,
                                   fuerza = 30,
                                   agilidad = 25,
                                   vitalidad = 80,
                                   energia = 80,
                                   exp = 20)

