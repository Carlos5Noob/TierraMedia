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
        "relaciones": detalles_personajes[nombre]["relaciones"]
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


def main():
    add_character()
    add_character()
    add_character()
    add_weapon_to_character()
    show_characters()


if __name__ == "__main__":
    main()
