from Servidor.clases import Item

# Los items por ahora no van a interferir, mas a delante veo como meto los efectos

anilloDeVida = Item(nombre='Anillo de vida',
                    descripcion='Aumenta ligeramente los puntos de salud',
                    equipado=False)

anilloDeMagia = Item(nombre='Anillo de magia',
                     descripcion='Aumenta ligeramente el mana',
                     equipado=False)

brazaleteDeFuerza = Item(nombre='Brazalete de fuerza',
                         descripcion='Aumenta la fuerza',
                         equipado=False)

guanteDeAgilidad = Item(nombre='Guante de agilidad',
                        descripcion='Aumenta la agilidad',
                        equipado=False)

items = [anilloDeVida, anilloDeMagia, brazaleteDeFuerza]