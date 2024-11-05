class Personaje():
    def __init__(self, nombre, raza, faccion, ubicacion, hp, equipamiento=None, relaciones=None):
        self.nombre = nombre
        self.raza = raza
        self.faccion = faccion
        self.ubicacion = ubicacion
        self.equipamiento = equipamiento
        self.relaciones = relaciones if not None else []
        self.hp = hp

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        if  isinstance(nombre, str):
            self.nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres. ")

    @property
    def raza(self):
        return self.raza

    @raza.setter
    def raza(self, raza):
        if isinstance(raza, str):
            self.raza = raza
        else:
            raise ValueError("La raza debe ser una cadena de caracteres. ")

    @property
    def faccion(self):
        return self.faccion

    @faccion.setter
    def faccion(self, faccion):
        if isinstance(faccion, str):
            self.faccion = faccion
        else:
            raise ValueError("La facción debe ser una cadena de caracteres. ")

    @property
    def ubicacion(self):
        return self.ubicacion

    @ubicacion.setter
    def ubicacion(self, ubicacion):
        if isinstance(ubicacion, str):
            self.ubicacion = ubicacion
        else:
            raise ValueError("La ubicación debe ser una cadena de caracteres. ")

    @property
    def equipamiento(self):
        return self.equipamiento

    @equipamiento.setter
    def equipamiento(self, equipamiento):
        if isinstance(equipamiento, str):
            self.equipamiento = equipamiento
        else:
            raise ValueError("El equipamiento debe ser una cadena de caracteres. ")

    @property
    def hp(self):
        return self.hp

    @hp.setter
    def hp(self, hp):
        if isinstance(hp, int):
            self.hp = hp
        else:
            raise ValueError("La salud del personaje (hp) ha de ser un número entero. ")

    @property
    def relaciones(self):
        return self.relaciones

    @relaciones.setter
    def relaciones(self, relaciones):
        if isinstance(relaciones, list):
            self.relaciones = relaciones
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
            pass # TODO