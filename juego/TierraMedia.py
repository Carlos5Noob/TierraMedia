""" from ..relations.relations import Relations
from character.Personaje import Personaje
from ubication.Ubication import Ubication
from Equipment.equipment import Equipment
from combat.combat import Combat
 """

from time import sleep
from random import randint

class Personaje():


    def __init__(self, nombre, raza, faccion, ubicacion, hp, equipamiento=None, relaciones=None):
        """
        Método constructor de la clase Personaje
        :param nombre: nombre del personaje
        :param raza: raza del personaje
        :param faccion: faccion del personaje
        :param ubicacion: ubicacion del personaje
        :param hp: salud total del personaje
        :param equipamiento: equipamiento del personaje
        :param relaciones: relaciones del personaje
        """
        self._nombre = nombre
        self._raza = raza
        self._faccion = faccion
        self._ubicacion = ubicacion
        self._equipamiento = equipamiento
        self._relaciones = relaciones if not None else []
        self._hp = hp


    # GETTERS AND SETTERS
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
        if isinstance(ubicacion, Ubication):
            self._ubicacion = ubicacion
        else:
            raise ValueError("La ubicación debe ser de la clase Ubication. ")

    @property
    def equipamiento(self):
        return self._equipamiento

    @equipamiento.setter
    def equipamiento(self, equipamiento):
        if isinstance(equipamiento, Equipment):
            self._equipamiento = equipamiento
        else:
            raise ValueError("El equipamiento debe ser de clase Equipamiento.  ")

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
        """
        Función para añadir un arma a un personaje
        :param equipamiento: arma de lc clase Equipment
        :return:
        """
        if isinstance(equipamiento, Equipment):
            self.equipamiento = equipamiento
        else:
            raise ValueError("El equipamiento debe ser de la clase Equipment.")

    def establecer_relacion(self, personaje, tipo_relacion, nivel_confianza):
        """
        Función que establece una nueva relación con un personaje
        :param personaje: personaje de la clase Personaje
        :param tipo_relacion: tipo de relación
        :param nivel_confianza: nivel de confianza de la relacion
        :return:
        """
        if isinstance(personaje, Personaje):
            self._relaciones.append(Relations(personaje, tipo_relacion, nivel_confianza))
        else:
            raise ValueError("El objeto personaje debe ser una instancia de la clase Personaje.")

    def mover(self, nueva_ubicacion):
        """
        Método para mover de una ubicación a un personaje
        :param nueva_ubicacion: nueva ubicación para el personaje
        :return:
        """
        if isinstance(nueva_ubicacion, Ubication):
            self.ubicacion = nueva_ubicacion
        else:
            raise ValueError("La ubicación debe ser de la clase Ubication.")

    def obtener_potencia_armma(self):
        """
        Método que devuelve la potencia del arma equipada del personaje
        :return:
        """
        if self.equipamiento == None:
            print(f"El personaje {self.nombre} no tiene ningún arma equipada. ")
        else:
            pass


class Combat:

    def __init__(self):
        """
        Método constructor de la clase Combat
        """
        pass

    def fight(self, ft1, ft2):
        """
        Función que simula un combate entre dos personajes de la clase Personaje
        :param ft1: personaje 1 de la clase Personaje
        :param ft2: personaje 2 de la clase Personaje
        :return:
        """

        print(f"Empieza el combate entre {ft1.nombre} y {ft2.nombre}: ")
 
        self.healing_before_battle(ft1)
        self.healing_before_battle(ft2)

        while ft1.hp > 0 and ft2.hp > 0:
            # Turno del primer personaje
            print(f"\nTurno de {ft1.nombre}")
            if not ft1.equipamiento:
                print(f"{ft1.nombre} no tiene un arma equipada y huye del combate.")
                break

            if self.attack(self.check_prob(ft1.equipamiento.equipment_name)):
                print(f"El ataque ha acertado, {ft1.nombre} ha causado {ft1.equipamiento.equipment_power} puntos de daño.")
                ft2.hp -= ft1.equipamiento.equipment_power
            else:
                print(f"El ataque de {ft1.nombre} ha fallado.")

            sleep(1.5)

            if ft2.hp <= 0:
                print(f"{ft2.nombre} ha perdido este combate.")
                break

            # Turno del segundo personaje
            print(f"\nTurno de {ft2.nombre}")
            if not ft2.equipamiento:
                print(f"{ft2.nombre} no tiene un arma equipada y huye del combate.")
                break

            if self.attack(self.check_prob(ft2.equipamiento.equipment_name)):
                print(f"El ataque ha acertado, {ft2.nombre} ha causado {ft2.equipamiento.equipment_power} puntos de daño.")
                ft1.hp -= ft2.equipamiento.equipment_power
            else:
                print(f"El ataque de {ft2.nombre} ha fallado.")

            sleep(1.5)

            if ft1.hp <= 0:
                print(f"{ft1.nombre} ha perdido este combate.")
                break

    def healing_before_battle(self, fighter):
        """Restaura los puntos de salud del luchador a 300 antes de la batalla."""
        fighter.hp = 300

    def attack(self, chance):
        """Determina si un ataque tiene éxito basado en la probabilidad dada."""
        return chance >= randint(1, 100)

    def check_prob(self, weapon_name):
        """Devuelve la probabilidad de éxito del ataque según el tipo de arma equipada."""
        attack_chance = 0
        if "sword" in weapon_name.lower():
            attack_chance = 50
        elif "dagger" in weapon_name.lower():
            attack_chance = 40
        elif "axe" in weapon_name.lower():
            attack_chance = 45
        elif "bow" in weapon_name.lower():
            attack_chance = 65
        elif "staff" in weapon_name.lower():
            attack_chance = 60
        elif "ring" in weapon_name.lower():
            attack_chance = 70
        return attack_chance



class Equipment():

    def __init__(self, equipment_name, equipment_type, equipment_power):
        """
        Método constructor de la clase Equipment
        :param equipment_name: nombre del arma
        :param equipment_type: tipo del arma
        :param equipment_power: potencia del arma
        """
        self._equipment_name = equipment_name
        self._equipment_type = equipment_type
        self._equipment_power = equipment_power

    # GETTERS AND SETTERS
    @property
    def equipment_name(self):
        return self._equipment_name

    @equipment_name.setter
    def equipment_name(self, equipment_name):
        if isinstance(equipment_name, str):
            self._equipment_name = equipment_name
        else:
            raise ValueError('El nombre del equipamiento debe ser una cadena de carácteres: ')

    @property
    def equipment_type(self):
        return self._equipment_type

    @equipment_type.setter
    def equipment_type(self, equipment_type):
        if isinstance(equipment_type, str):
            self._equipment_type = equipment_type
        else:
            raise ValueError('El tipo de equipamiento debe ser una cadena de carácteres: ')

    @property
    def equipment_power(self):
        return self._equipment_power

    @equipment_power.setter
    def equipment_power(self, equipment_power):
        if isinstance(equipment_power, int):
            self._equipment_power = equipment_power
        else:
            raise ValueError('El poder del arma debe ser una cadena numérica: ')

    def is_a_weapon(self, equipment_type):
        """
        Método que verifica si un arma es de la clase Equipment
        :param equipment_type: arma
        :return:
        """
        if isinstance(equipment_type, Equipment):
            return True
        else:
            return False
        


class Relations:
    def __init__(self, Personaje, tipo_relacion, nivel_confianza ):
        """
        Método constructor de la clase Relations
        :param Personaje: personaje de la clase Personaje
        :param tipo_relacion: tipo relacion
        :param nivel_confianza: nivel confianza
        """
        self._Personaje=Personaje
        self._tipo_relacion=tipo_relacion
        self._nivel_confianza=nivel_confianza

    # GETTERS AND SETTERS
    @property
    def Personaje(self):
        return self._Personaje

    @Personaje.setter
    def nombre(self, Personaje):
        if  isinstance(Personaje, str):
            self._Personaje = Personaje
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres. ")

    @property
    def tipo_relacion(self):
        return self._tipo_relacion

    @tipo_relacion.setter
    def tipo_relacion(self, tipo_relacion):
        if isinstance(tipo_relacion, str):
            self._tipo_relacion=tipo_relacion

    @property
    def nivel_confianza(self):
        return self._nivel_confianza

    @nivel_confianza.setter
    def nivel_confianza(self, nivel_confianza):
        if isinstance(nivel_confianza, str):
            self._nivel_confianza=nivel_confianza


class Ubication:
    def __init__(self, tipo):
        """
        Método constructor
        :param tipo: tipo ubicacion
        """
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo


class TierraMedia:

    def __init__(self, personajes, facciones):
        """
        Método constructor de la clase TierraMedia
        :param personajes: lista donde se almacenan los personajes de la clase Personaje
        :param facciones: lista de facciones
        """
        self.personajes = personajes
        self.facciones = facciones

    def añadir_relacion(self, personaje, relacion):
        """
        Método que añade una nueva relacion a un personaje de la lista
        :param personaje:
        :param relacion:
        :return:
        """
        if personaje not in self.personajes:
            raise Exception("El personaje no está en la lista de personajes. ")
        else:
            pass

    def cambiar_ubicacion(self, personaje, ubicacion):
        """
        Método que cambia la ubicación a un personaje
        :param personaje:
        :param ubicacion:
        :return:
        """
        if personaje not in self.personajes:
            raise Exception("El personaje no está en la lista de personajes. ")
        else:
             personaje.ubicacion = ubicacion
             print("Ubicación añadida. ")

    def registrar_personaje(self, personaje):
        """
        Función que registrar un nuevo personaje a la lista de personajes
        :param self:
        :param personaje:
        :return:
        """
        if isinstance(personaje, Personaje):
            self.personajes.append(personaje)
            print(f"Personaje {personaje.nombre} añadido. ")
        else:
            raise Exception("El personaje debe ser de la clase Personaje. ")

    def añadir_equipamiento(self, personaje, equipamiento):
        """
        Función que añade un equipamiento a un personaje almacenado en la lista
        :param self:
        :param personaje:
        :param equipamiento:
        :return:
        """
        if personaje not in self.personajes:
            raise Exception("El personaje no está en la lista de personajes. ")
        else:
            if isinstance(equipamiento, Equipment):
                personaje.equipamiento = equipamiento
                print(f"Arma equipada al personaje {personaje.nombre}.")
            else:
                raise Exception("El equipamiento no es de la clase Equipamiento. ")
    
    def listar_personajes(self):
        """
        Método para listar todos los personajes de la lista
        :param self:
        :return:
        """
        if not self.personajes:
            print("No hay personajes en la lista. ")
            return
        
        else: 
            print("Lista de personajes en TierraMedia:")

            for personaje in self.personajes:
                print(f"\nNombre: {personaje.nombre}")
                print(f"Raza: {personaje.raza}")
                print(f"Facción: {personaje.faccion}")
                print(f"Ubicación: {personaje.ubicacion}")
                print(f"HP: {personaje.hp}")
                if personaje.equipamiento:
                    print(f"Equipamiento: {personaje.equipamiento.equipment_name} (Tipo: {personaje.equipamiento.equipment_type}, Poder: {personaje.equipamiento.equipment_power})")
                else:
                    print("Equipamiento: Ninguno")
                if personaje.relaciones:
                    print("Relaciones:")
                    for relacion in personaje.relaciones:
                        print(f"  - {relacion.personaje.nombre}, Tipo: {relacion.tipo_relacion}, Nivel de Confianza: {relacion.nivel_confianza}")
                else:
                    print("Relaciones: Ninguna")
    
    def combate(self, fighter1, figther2):
        """
        Método que simula un combate entre dos personajes de la clase Personaje
        :param self:
        :param fighter1:
        :param figther2:
        :return:
        """

        if fighter1 not in self.personajes or figther2 not in self.personajes:
            raise Exception("Uno o ambos personajes no están registrados en TierraMedia.")
        
        else:       
            combat = Combat()
            combat.fight(fighter1, figther2)


def main():
    """
    Método main que es el que se ejecuta
    :return:
    """
    tierra_media = TierraMedia([], [])

    try:
        personaje1 = Personaje("Aragorn", "Humano", "Gondor", "Minas Tirith", 300)
        personaje2 = Personaje("Legolas", "Elfo", "Elfos del Bosque", "Bosque Negro", 300)

        tierra_media.registrar_personaje(personaje1)
        tierra_media.registrar_personaje(personaje2)

        arma1 = Equipment("Anduril Sword", "Sword", 70)
        arma2 = Equipment("Bow", "Bow", 50)

        tierra_media.añadir_equipamiento(personaje1, arma1)
        tierra_media.añadir_equipamiento(personaje2, arma2)

        tierra_media.listar_personajes()

        tierra_media.combate(personaje1, personaje2)

    except Exception as e:
        print(e)

if __name__ == "__main__": 
    main()
