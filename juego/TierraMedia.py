from character.Personaje import Personaje
from Equipment import equipment

class TierraMedia:

    def __init__(self, personajes, facciones):
        self.personajes = personajes
        self.facciones = facciones
        self.characters = {}

    def registrar_personaje(self, nombre, raza, faccion, ubicacion, hp):
        nuevo_personaje = Personaje(nombre, raza, hp, faccion, ubicacion)
        self.characters[nombre] = {
            "raza": raza,
            "hp": hp,
            "faccion": faccion,
            "ubicacion": ubicacion
        }
        print(f"Personaje: {nombre} añadido. ")

    def añadir_equipamiento(self, nombre_personaje, equipamiento):
        if nombre_personaje not in self.characters:
            raise Exception("El personaje no está en la lista de personajes. ")
        else:
            if isinstance(equipamiento, equipment):
                self.characters[nombre_personaje]["equipamiento"] = equipamiento
                print(f"Arma {equipamiento} equipada al personaje {nombre_personaje}")
            else:
                raise Exception("El equipamiento no es de la clase Equipamiento. ")
