from character import Personaje

class Relations:
    def __init__(self, Personaje, tipo_relacion, nivel_confianza ):
        self.Personaje=Personaje
        self.tipo_relacion=tipo_relacion
        self.nivel_confianza=nivel_confianza

    @property
    def Personaje(self):
        return self.Personaje

    @Personaje.setter
    def nombre(self, Personaje):
        if  isinstance(Personaje, str):
            self.Personaje = Personaje
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres. ")

    @property
    def tipo_relacion(self):
        return self.tipo_relacion

    @tipo_relacion.setter
    def tipo_relacion(self, tipo_relacion):
        if isinstance(tipo_relacion, str):
            self.tipo_relacion=tipo_relacion

    @property
    def nivel_confianza(self):
        return self.nivel_confianza

    @nivel_confianza.setter
    def nivel_confianza(self, nivel_confianza):
        if isinstance(nivel_confianza, str):
            self.nivel_confianza=nivel_confianza