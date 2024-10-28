import random

characters = {}

personajes_disponibles = ["Aragorn", "Legolas", "Gimli", "Frodo", "Boromir", "Saruman", "Galadriel", "Sauron"]

detalles_personajes = {
    "Aragorn": {"raza": "Humano", "faccion": "La comunidad del anillo", "ubicacion": "Rivendel",
                "relaciones": {"personaje": "Legolas", "tipo": "Amigo", "nivel_confianza": 10}},
    "Legolas": {"raza": "Elfo", "faccion": "La comunidad del anillo", "ubicacion": "Bosque Negro",
                "relaciones": {"personaje": "Aragorn", "tipo": "Amigo", "nivel_confianza": 10}},
    "Gimli": {"raza": "Enano", "faccion": "La comunidad del anillo", "ubicacion": "Rivendel",
              "relaciones": {"personaje": "Aragorn", "tipo": "Amigo", "nivel_confianza": 9}},
    "Frodo": {"raza": "Hobbit", "faccion": "La comunidad del anillo", "ubicacion": "Hobbiton",
              "relaciones": {"personaje": "Boromir", "tipo": "Neutral", "nivel_confianza": 5}},
    "Boromir": {"raza": "Humano", "faccion": "La comunidad del anillo", "ubicacion": "Rivendel",
                "relaciones": {"personaje": "Frodo", "tipo": "Neutral", "nivel_confianza": 5}},
    "Saruman": {"raza": "Humano", "faccion": "Isengard", "ubicacion": "Isengard",
                "relaciones": {"personaje": "Galadriel", "tipo": "Enemigo", "nivel_confianza": 2}},
    "Galadriel": {"raza": "Elfo", "faccion": "Lothlórien", "ubicacion": "Bosque Negro",
                  "relaciones": {"personaje": "Saruman", "tipo": "Enemigo", "nivel_confianza": 2}},
    "Sauron": {"raza": "Humano", "faccion": "Mordor", "ubicacion": "Mordor",
               "relaciones": {"personaje": "Aragorn", "tipo": "Enemigo", "nivel_confianza": 1}}
}

weapon = ["Espada Andúril", 'Arco de Galadriel', 'Hacha de Gimli', 'Daga de Frodo', 'Báculo de Saruman', 'Anillo Único',
          'Espada de Boromir']
type_weapon = {weapon[0]: 'Espada', weapon[1]: 'Arco', weapon[2]: 'Hacha', weapon[3]: 'Daga', weapon[4]: 'Bastón',
               weapon[5]: 'Anillo', weapon[6]: 'Espada'}
weapon_power = {weapon[0]: 100, weapon[1]: 60, weapon[2]: 80, weapon[3]: 70, weapon[4]: 80, weapon[5]: 60,
                weapon[6]: 50}


def add_character():
    nombre = input(
        "Introduce el nombre del personaje (Aragorn, Legolas, Gimli, Frodo, Boromir, Saruman, Galadriel, Sauron): ").capitalize()

    if nombre not in personajes_disponibles:
        print("El nombre introducido no es válido.")
        return


    characters[nombre] = {
        "raza": detalles_personajes[nombre]["raza"],
        "faccion": detalles_personajes[nombre]["faccion"],
        "ubicacion": detalles_personajes[nombre]["ubicacion"],
        "relaciones": detalles_personajes[nombre]["relaciones"],
        "hp": 300
    }
    print(f"Personaje {nombre} añadido.")


def add_weapon_to_character():
    personaje = input("Introduce un personaje al que quieras asignar un arma: ").capitalize()

    if personaje not in characters:
        print("El personaje seleccionado no existe.")
        return

    arma = input(f"Introduce el arma que quieras añadir a {personaje}: ").strip()

    if arma not in weapon:
        print("El arma seleccionada no existe.")
        return


    characters[personaje]["equipamiento"] = {
        "nombre": arma,
        "tipo": type_weapon[arma],
        "potencia": weapon_power[arma]
    }
    print(f"Arma '{arma}' añadida correctamente al personaje {personaje}.")


def show_characters():
    if not characters:
        print("No hay ningún personaje en el sistema.")
        return

    for nombre, detalles in characters.items():
        print(f"\nPersonaje: {nombre}")
        print("  Raza:", detalles["raza"])
        print("  Facción:", detalles["faccion"])
        print("  Ubicación:", detalles["ubicacion"])


        if "equipamiento" in detalles:
            equipamiento = detalles["equipamiento"]
            print("  Equipamiento:")
            print(f"    - Nombre: {equipamiento['nombre']}")
            print(f"    - Tipo: {equipamiento['tipo']}")
            print(f"    - Potencia: {equipamiento['potencia']}")
        else:
            print("  Equipamiento: Ninguno")

        relaciones = detalles["relaciones"]
        print("  Relaciones:")
        print(f"    - Personaje: {relaciones['personaje']}")
        print(f"    - Tipo: {relaciones['tipo']}")
        print(f"    - Nivel de confianza: {relaciones['nivel_confianza']}")

def show_characters_per_faction(faction):
    if not characters:
        print(f"No hay ningún personaje en el sistema.")
        return

    for nombre, detalles in characters.items():
        if detalles["faccion"] == faction:
            print(f"\nPersonaje: {nombre}")
            print("  Raza:", detalles["raza"])
            print("  Facción:", detalles["faccion"])
            print("  Ubicación:", detalles["ubicacion"])

            if "equipamiento" in detalles:
                equipamiento = detalles["equipamiento"]
                print("  Equipamiento:")
                print(f"    - Nombre: {equipamiento['nombre']}")
                print(f"    - Tipo: {equipamiento['tipo']}")
                print(f"    - Potencia: {equipamiento['potencia']}")
            else:
                print("  Equipamiento: Ninguno")

            relaciones = detalles["relaciones"]
            print("  Relaciones:")
            print(f"    - Personaje: {relaciones['personaje']}")
            print(f"    - Tipo: {relaciones['tipo']}")
            print(f"    - Nivel de confianza: {relaciones['nivel_confianza']}")

def show_characters_per_equipment(equipment):
    if not characters:
        print(f"No hay ningún personaje en el sistema.")
        return

    for nombre, detalles in characters.items():
        if "equipamiento" in detalles and detalles["equipamiento"]["nombre"] == equipment:
            print(f"\nPersonaje: {nombre}")
            print("  Raza:", detalles["raza"])
            print("  Facción:", detalles["faccion"])
            print("  Ubicación:", detalles["ubicacion"])

            equipamiento = detalles["equipamiento"]
            print("  Equipamiento:")
            print(f"    - Nombre: {equipamiento['nombre']}")
            print(f"    - Tipo: {equipamiento['tipo']}")
            print(f"    - Potencia: {equipamiento['potencia']}")

            relaciones = detalles["relaciones"]
            print("  Relaciones:")
            print(f"    - Personaje: {relaciones['personaje']}")
            print(f"    - Tipo: {relaciones['tipo']}")
            print(f"    - Nivel de confianza: {relaciones['nivel_confianza']}")




def fight(fighter1_name, fighter2_name):
    # Convertimos los nombres a diccionarios de personaje
    fighter1 = characters.get(fighter1_name.capitalize())
    fighter2 = characters.get(fighter2_name.capitalize())

    # Verificamos que ambos personajes existen en el diccionario `characters`
    if not fighter1 or not fighter2:
        print("Uno o ambos personajes no existen.")
        return

    # Curamos a los personajes antes de la batalla
    healing_before_battle(fighter1)
    healing_before_battle(fighter2)

    print(f"Empieza el combate entre {fighter1_name} y {fighter2_name}")
    while fighter1["hp"] > 0 and fighter2["hp"] > 0:
        print(f"Turno de {fighter1_name}")

        # Verificamos si el personaje tiene un arma equipada
        if "equipamiento" not in fighter1:
            print(f"{fighter1_name} no tiene un arma equipada y no puede atacar.")
            break
        if "equipamiento" not in fighter2:
            print(f"{fighter2_name} no tiene un arma equipada y no puede atacar.")
            break

        # Ataque de fighter1 a fighter2
        if attack(check_prob(fighter1["equipamiento"]["nombre"])):
            print(
                f"El ataque ha acertado, {fighter1_name} ha causado {fighter1['equipamiento']['potencia']} puntos de daño.")
            fighter2["hp"] -= fighter1["equipamiento"]["potencia"]
        else:
            print(f"El ataque de {fighter1_name} ha fallado, mala suerte!")

        # Verificamos si fighter2 sigue vivo
        if fighter2["hp"] <= 0:
            print(f"{fighter2_name} ha perdido este combate")
            break

        print(f"Turno de {fighter2_name}")

        # Ataque de fighter2 a fighter1
        if attack(check_prob(fighter2["equipamiento"]["nombre"])):
            print(
                f"El ataque ha acertado, {fighter2_name} ha causado {fighter2['equipamiento']['potencia']} puntos de daño.")
            fighter1["hp"] -= fighter2["equipamiento"]["potencia"]
        else:
            print(f"El ataque de {fighter2_name} ha fallado, mala suerte!")

        # Verificamos si fighter1 sigue vivo
        if fighter1["hp"] <= 0:
            print(f"{fighter1_name} ha perdido este combate")
            break

def healing_before_battle(fighter):
    # Restauramos la salud antes de la batalla
    fighter["hp"] = 300

def attack(chance):
    return chance >= random.randint(1, 100)

def check_prob(weapon_name):
    # Determinamos la probabilidad de ataque en base al nombre del arma
    attack_chance = 0
    if "espada" in weapon_name.lower():
        attack_chance = 50
    elif "daga" in weapon_name.lower():
        attack_chance = 40
    elif "hacha" in weapon_name.lower():
        attack_chance = 45
    elif "arco" in weapon_name.lower():
        attack_chance = 65
    elif "baston" in weapon_name.lower():
        attack_chance = 60
    elif "anillo" in weapon_name.lower():
        attack_chance = 70
    return attack_chance



def show_menu():
        print("""\n----- Menu Juego Tierra Media -----
        1. Registrar un nuevo personaje
        2. Añadir equipamiento a un personaje
        3. Equipar un arma a un personaje
        4. Establecer relaciones entre personajes
        5. Mover un personaje a una nueva localización
        6. Simular una batalla entre dos personajes
        7. Listar personajes por facción
        8. Buscar personajes por equipamiento
        9. Mostrar todos los personajes
        10. Salir
        -------------------------------------------------
        Haga su eleccion \n""")





def main():
    continuar = True

    while continuar:
        opcion = 0
        show_menu()
        try:
            while opcion <=0 or opcion >10:
                print("Introduzca un número del 1 al 10")
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
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("Has elegido la opción de combate entre dos personajes. ")
                print("Aquí tienes una lista de todos los personajes: \n")
                show_characters()
                character1 = input("Introduce el personaje 1: ")
                character2 = input("Introduce el personaje 2: ")
                fight(character1, character2)
            case 7:
                print("Has elegido mostrar personajes por facción.")
                faction = input("Introduce la facción que quieras buscar: ")
                show_characters_per_faction()
            case 8:
                print("Has elegido mostrar personajes por equipamiento.\n")
                equipment = input("Introduce el equipamiento que quieras buscar: ")
                show_characters_per_equipment(equipment)
            case 9:
                print("Has elegido la opción de mostrar todos los personajes: \n")
                show_characters()
            case 10:
                continuar = False
                return print(f"Saliendo del programa...")


if __name__ == "__main__":
    main()
