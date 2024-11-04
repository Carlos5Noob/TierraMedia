import random
import time

characters = {}

available_characters = ["Aragorn", "Legolas", "Gimli", "Frodo", "Boromir", "Saruman", "Galadriel", "Sauron"]

character_details = {
    "Aragorn": {"race": "Human", "faction": "Fellowship", "location": "Rivendell",
                "relationships": [{"character": "Legolas", "type": "Friend", "trust_level": 10}]},
    "Legolas": {"race": "Elf", "faction": "Fellowship", "location": "Mirkwood", "relationships": []},
    "Gimli": {"race": "Dwarf", "faction": "Fellowship", "location": "Moria", "relationships": []},
    "Frodo": {"race": "Hobbit", "faction": "Fellowship", "location": "Shire", "relationships": []},
    "Boromir": {"race": "Human", "faction": "Gondor", "location": "Minas Tirith", "relationships": []},
    "Saruman": {"race": "Maiar", "faction": "Isengard", "location": "Isengard", "relationships": []},
    "Galadriel": {"race": "Elf", "faction": "Lothlórien", "location": "Lothlórien", "relationships": []},
    "Sauron": {"race": "Maiar", "faction": "Mordor", "location": "Mordor", "relationships": []},
}

weapons = ["Anduril Sword", "Galadriel's Bow", "Gimli's Axe", "Frodo's Dagger", "Saruman's Staff", "One Ring", "Boromir's Sword"]
weapon_types = {weapons[0]: 'Sword', weapons[1]: 'Bow', weapons[2]: 'Axe', weapons[3]: 'Dagger', weapons[4]: 'Staff', weapons[5]: 'Ring', weapons[6]: 'Sword'}
weapon_powers = {weapons[0]: 100, weapons[1]: 60, weapons[2]: 80, weapons[3]: 70, weapons[4]: 80, weapons[5]: 60, weapons[6]: 50}

locations = ("Rivendell", "Shire", "Minas Tirith", "Mordor", "Isengard", "Mirkwood", "Lothlórien")

def change_location(name):
    """
    Cambia la ubicación de un personaje existente.

    :param name: str, nombre del personaje
    """
    character = characters.get(name.capitalize())
    if not character:
        print(f"{name} no existe en el sistema.")
        return

    print(f"Ubicación actual de {name}: {character['location']}")
    new_location = input("Nueva ubicación: ").capitalize()
    while new_location not in locations:
        new_location = input(f"{new_location} no es válido. Introduzca otra ubicación: ").capitalize()

    if new_location != character["location"]:
        character["location"] = new_location
        print(f"{name} ha sido trasladado a {new_location}")
    else:
        print(f"{name} ya se encuentra en {new_location}")

def add_relationship(name):
    """
    Añade una relación entre dos personajes.

    :param name: str, nombre del personaje al que se añadirá la relación
    """
    related_name = input("Nombre del personaje con quien tendrá relación: ").capitalize()
    if related_name not in available_characters:
        print("Personaje no existe. Intente nuevamente.")
        return

    relationship_type = input("Tipo de relación: ")
    trust_level = int(input("Nivel de confianza: "))

    characters[name]["relationships"].append({
        "character": related_name,
        "type": relationship_type,
        "trust_level": trust_level
    })
    print(f"Relación añadida entre {name} y {related_name}")

def add_character():
    """
    Añade un nuevo personaje al sistema con detalles predefinidos.
    """
    name = input("Elija el nombre de un personaje de esta lista (Aragorn, Legolas, Gimli, Frodo, Boromir, Saruman, Galadriel, Sauron): ").lower().capitalize()
    if name not in available_characters:
        print("El nombre no es válido.")
        return

    characters[name] = character_details[name]
    characters[name]["hp"] = 300
    print(f"Personaje {name} añadido.")

def add_weapon_to_character():
    """
    Asigna un arma a un personaje existente en el sistema.
    """
    name = input("Nombre del personaje: ").lower().capitalize()
    if name not in characters:
        print("Personaje no existe.")
        return

    weapon_name = input("Nombre del arma (Anduril Sword, Galadriel's Bow, Gimli's Axe, Frodo's Dagger, Saruman's Staff, One Ring, Boromir's Sword): ").strip()
    if weapon_name not in weapons:
        print("El arma no existe.")
        return

    characters[name]["equipment"] = {
        "name": weapon_name,
        "type": weapon_types[weapon_name],
        "power": weapon_powers[weapon_name]
    }
    print(f"Arma '{weapon_name}' asignada a {name}.")

def show_characters():
    """
    Muestra todos los personajes en el sistema.
    """
    if not characters:
        print("No hay personajes en el sistema.")
        return

    for name, details in characters.items():
        print(f"\nPersonaje: {name}")
        print("  Raza:", details["race"])
        print("  Facción:", details["faction"])
        print("  Ubicación:", details["location"])

        if "equipment" in details:
            equip = details["equipment"]
            print("  Equipamiento:")
            print(f"    - Nombre: {equip['name']}")
            print(f"    - Tipo: {equip['type']}")
            print(f"    - Potencia: {equip['power']}")
        else:
            print("  Equipamiento: Ninguno")

        print("  Relaciones:")
        for relation in details["relationships"]:
            print(f"    - Personaje: {relation['character']}")
            print(f"    - Tipo: {relation['type']}")
            print(f"    - Nivel de confianza: {relation['trust_level']}")

def fight(fighter1_name, fighter2_name):

    """
    Inicia un combate entre dos personajes.

    Args:
        fighter1_name (str): Nombre del primer luchador.
        fighter2_name (str): Nombre del segundo luchador.
    """

    fighter1 = characters.get(fighter1_name.capitalize())
    fighter2 = characters.get(fighter2_name.capitalize())

    if not fighter1 or not fighter2:
        print("Uno o ambos personajes no existen.")
        return

    healing_before_battle(fighter1)
    healing_before_battle(fighter2)

    print(f"Empieza el combate entre {fighter1_name} y {fighter2_name}")

    while fighter1["hp"] > 0 and fighter2["hp"] > 0:
        print(f"\nTurno de {fighter1_name}")

        if "equipment" not in fighter1:
            print(f"{fighter1_name} no tiene un arma equipada y no puede atacar, por lo tanto huye del combate.")
            break
        if "equipment" not in fighter2:
            print(f"{fighter2_name} no tiene un arma equipada y no puede atacar, por lo tanto huye del combate.")
            break
        time.sleep(0.75)
        if attack(check_prob(fighter1["equipment"]["name"])):
            print(
                f"El ataque ha acertado, {fighter1_name} ha causado {fighter1['equipment']['power']} puntos de daño.")
            fighter2["hp"] -= fighter1["equipment"]["power"]
        else:
            print(f"El ataque de {fighter1_name} ha fallado, mala suerte!")

        time.sleep(1.5)

        if fighter2["hp"] <= 0:
            print(f"{fighter2_name} ha perdido este combate")
            break

        time.sleep(1)

        print(f"\nTurno de {fighter2_name}")

        time.sleep(0.75)

        if attack(check_prob(fighter2["equipment"]["name"])):
            print(
                f"El ataque ha acertado, {fighter2_name} ha causado {fighter2['equipment']['power']} puntos de daño.")
            fighter1["hp"] -= fighter2["equipment"]["power"]
        else:
            print(f"El ataque de {fighter2_name} ha fallado, mala suerte!")

        time.sleep(1.5)

        if fighter1["hp"] <= 0:
            print(f"{fighter1_name} ha perdido este combate")
            break

        time.sleep(1.5)
def healing_before_battle(fighter):

    """
    Restaura los puntos de salud del luchador a 300 antes de la batalla.

    Args:
        fighter (dict): Diccionario que contiene la información del luchador.
    """

    fighter["hp"] = 300

def attack(chance):

    """
    Determina si un ataque tiene éxito basado en la probabilidad dada.

    Args:
        chance (int): Porcentaje de probabilidad de que el ataque tenga éxito.

    Returns:
        bool: True si el ataque tiene éxito, False en caso contrario.
    """

    return chance >= random.randint(1, 100)

def check_prob(weapon_name):

    """
    Devuelve la probabilidad de éxito del ataque según el tipo de arma equipada.

    Args:
        weapon_name (str): Nombre del arma equipada.

    Returns:
        int: Probabilidad de éxito del ataque.
    """

    attack_chance = 0
    if "sword" in weapon_name.lower():
        attack_chance = 50
    if "dagger" in weapon_name.lower():
        attack_chance = 40
    if "axe" in weapon_name.lower():
        attack_chance = 45
    if "bow" in weapon_name.lower():
        attack_chance = 65
    if "staff" in weapon_name.lower():
        attack_chance = 60
    if "ring" in weapon_name.lower():
        attack_chance = 70
    return attack_chance


def show_characters_per_faction(faction):

    """
    Muestra los personajes que pertenecen a una facción específica.

    Args:
        faction (str): Nombre de la facción para filtrar los personajes.
    """

    if not characters:
        print(f"No hay ningún personaje en el sistema.")
        return

    for nombre, detalles in characters.items():
        if detalles["faction"] == faction:
            print(f"\nPersonaje: {nombre}")
            print("  Raza:", detalles["race"])
            print("  Facción:", detalles["faction"])
            print("  Ubicación:", detalles["location"])

            if "equipment" in detalles:
                equipamiento = detalles["equipment"]
                print("  Equipamiento:")
                print(f"    - Nombre: {equipamiento['name']}")
                print(f"    - Tipo: {equipamiento['type']}")
                print(f"    - Potencia: {equipamiento['power']}")
            else:
                print("  Equipamiento: Ninguno")

            print("  Relaciones:")
            for relacion in detalles["relationships"]:
                print(f"    - Personaje: {relacion['character']}")
                print(f"    - Tipo: {relacion['type']}")
                print(f"    - Nivel de confianza: {relacion['trust_level']}")

def show_characters_per_equipment(equipment):

    """
    Muestra los personajes que tienen un equipamiento específico.

    Args:
        equipment (str): Nombre del equipamiento para filtrar los personajes.
    """

    if not characters:
        print(f"No hay ningún personaje en el sistema.")
        return

    for nombre, detalles in characters.items():
        if "equipment" in detalles and detalles["equipment"]["name"] == equipment:
            print(f"\nPersonaje: {nombre}")
            print("  Raza:", detalles["race"])
            print("  Facción:", detalles["faction"])
            print("  Ubicación:", detalles["location"])

            equipamiento = detalles["equipment"]
            print("  Equipamiento:")
            print(f"    - Nombre: {equipamiento['name']}")
            print(f"    - Tipo: {equipamiento['type']}")
            print(f"    - Potencia: {equipamiento['power']}")

            print("  Relaciones:")
            for relacion in detalles["relationships"]:
                print(f"    - Personaje: {relacion['character']}")
                print(f"    - Tipo: {relacion['type']}")
                print(f"    - Nivel de confianza: {relacion['trust_level']}")


def show_menu():
    """
    Muestra el menú principal del juego.
    """
    print("""\n----- Menu Juego Tierra Media -----
    1. Registrar un nuevo personaje
    2. Añadir equipamiento a un personaje
    3. Establecer relaciones entre personajes
    4. Mover un personaje a una nueva localización
    5. Simular una batalla entre dos personajes
    6. Listar personajes por facción
    7. Buscar personajes por equipamiento
    8. Mostrar todos los personajes
    9. Salir
    -------------------------------------------------
    Haga su eleccion \n""")
def main():
    """
    Función principal del juego.
    """
    salir = True

    while salir:
        opcion = 0
        show_menu()
        try:
            while opcion <= 0 or opcion > 9:
                print("Introduzca un número del 1 al 9")
                opcion = int(input())
        except ValueError:
            print("Opcion no válida, introduzca un número")

        match opcion:
            case 1:
                print("Has elegido la opción añadir personaje.")
                add_character()
            case 2:
                print("Has elegido la opción añadir arma a un personaje.\n")
                add_weapon_to_character()
            case 3:
                personaje = input(
                    "Introduce el nombre del personaje al que quieres añadir una nueva relación: ").lower().capitalize()
                while personaje not in available_characters:
                    personaje = input("Personaje no existe. Introduzca un personaje válido: ")
                add_relationship(personaje)
            case 4:
                print("Has elegido la opción de modificar la localización de un personaje. ")
                pj = input(f"Elige el personaje al cuál quiera cambiar su ubicación: ")
                while pj not in characters:
                    pj = input(
                        f"El personaje seleccionado no se encuentra en estas tierras, seleccione otro guerrero. ")
                change_location(pj)
            case 5:
                print("Has elegido la opción de combate entre dos personajes. ")
                print("Aquí tienes una lista de todos los personajes: \n")
                show_characters()
                character1 = input("Introduce el personaje 1: ")
                character2 = input("Introduce el personaje 2: ")
                fight(character1, character2)
            case 6:
                print("Has elegido mostrar personajes por facción.")
                faction = input("Introduce la facción que quieras buscar: ")
                show_characters_per_faction(faction)
            case 7:
                print("Has elegido mostrar personajes por equipamiento.\n")
                equipment = input("Introduce el equipamiento que quieras buscar: ")
                show_characters_per_equipment(equipment)
            case 8:
                print("Has elegido la opción de mostrar todos los personajes: \n")
                show_characters()
            case 9:
                salir = False
                return print(f"Saliendo del programa...")

if __name__ == "__main__":
    main()
