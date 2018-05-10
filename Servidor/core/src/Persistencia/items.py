from Servidor.core.src.Entidades.Item import Item

# Los items por ahora no van a interferir, mas a delante veo como meto los efectos

anilloDeVida = Item(nombre='Anillo de vida',
                    descripcion='Aumenta ligeramente los puntos de salud',
                    equipado=False)

anilloDeMagia = Item(nombre='Anillo de magia',
                     descripcion='Aumenta ligeramente el mana',
                     equipado=False)

items = [anilloDeVida, anilloDeMagia]
