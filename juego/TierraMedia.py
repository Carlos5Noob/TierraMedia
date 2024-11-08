from relations import relations
from character import Personaje
from ubication import Ubication

class TierraMedia:

    def __init__(self, personajes, facciones):
        self.personajes = personajes
        self.facciones = facciones
        self.characters = {}

    def añadir_relacion(self, nombre, relaciones, tipo_relacion, nivel_confianza):
        nueva_relacion = relations.relations[nombre, tipo_relacion, nivel_confianza]
        self.characters[nombre]["relacion"] = nueva_relacion

        print(f"{nombre} relacionado con {nombre}, el tipo es {tipo_relacion} y su nivel de confianza es {nivel_confianza}")

    def cambiar_ubicacion(self, nombre, ubicacion):
        nueva_ubicacion = Ubication.Ubication[nombre, ubicacion]
        self.characters[nombre]["tipo"] = nueva_ubicacion

        print(f"{nombre} se ha desplazado a {ubicacion}")
