from Equipment import equipment
from Equipment.equipment import Equipment
from ubication import Ubication

class Personaje():
    def __init__(self, nombre, raza, faccion, ubicacion, hp, equipamiento=None, relaciones=None):
        self._nombre = nombre
        self._raza = raza
        self._faccion = faccion
        self._ubicacion = ubicacion
        self._equipamiento = equipamiento
        self._relaciones = relaciones if not None else []
        self._hp = hp

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if  isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres. ")

    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, raza):
        if isinstance(raza, str):
            self._raza = raza
        else:
            raise ValueError("La raza debe ser una cadena de caracteres. ")

    @property
    def faccion(self):
        return self._faccion

    @faccion.setter
    def faccion(self, faccion):
        if isinstance(faccion, str):
            self._faccion = faccion
        else:
            raise ValueError("La facción debe ser una cadena de caracteres. ")

    @property
    def ubicacion(self):
        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, ubicacion):
        if isinstance(ubicacion, str):
            self._ubicacion = ubicacion
        else:
            raise ValueError("La ubicación debe ser una cadena de caracteres. ")

    @property
    def equipamiento(self):
        return self._equipamiento

    @equipamiento.setter
    def equipamiento(self, equipamiento):
        if isinstance(equipamiento, str):
            self._equipamiento = equipamiento
        else:
            raise ValueError("El equipamiento debe ser una cadena de caracteres. ")

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        if isinstance(hp, int):
            self._hp = hp
        else:
            raise ValueError("La salud del personaje (hp) ha de ser un número entero. ")

    @property
    def relaciones(self):
        return self._relaciones

    @relaciones.setter
    def relaciones(self, relaciones):
        if isinstance(relaciones, list):
            self._relaciones = relaciones
        else:
            raise ValueError("Las relaciones han de ser una lista. ")

    def añadir_equipamiento(self, equipamiento):
        if isinstance(equipamiento, Equipment):
            self.equipamiento = equipamiento
        else:
            raise ValueError("El equipamiento debe ser de la clase Equipment. ")

    def establecer_relacion(self, personaje, tipo_relacion, nivel_confianza):
        self.relaciones.append(personaje, tipo_relacion, nivel_confianza)

    def mover(self, nueva_ubicacion):
        if isinstance(nueva_ubicacion, Ubication):
            self.ubicacion = nueva_ubicacion
        else:
            raise ValueError("La ubicación debe ser de la clase Ubication. ")

    def obtener_potencia_armma(self):
        if self.equipamiento == None:
            print(f"El personaje {self.nombre} no tiene ningún arma equipada. ")
        else:
            pass