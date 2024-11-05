class TierraMedia:
    def __init__(self, personajes, facciones):
        self.personajes = personajes
        self.facciones = facciones

    def registrar_personaje(self, nombre, raza, faccion, ubicacion):
        nuevo_personaje