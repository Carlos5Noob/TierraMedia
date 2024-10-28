characters = {}

personajes_disponibles = ["Aragorn", "Legolas", "Gimli", "Frodo", "Boromir", "Saruman", "Galadriel", "Sauron"]
detalles_personajes = {"Aragorn":
                               {"raza": "Humano",
                                "faccion": "La comunidad del anillo",
                                "ubicacion": "Rivendel", 
                                "equipamiento": {"nombre": "Andúril", "tipo": "Espada", "potencia": 80},
                                "relaciones": {"personaje": "Legolas", "tipo": "Amigo", "nivel_confianza": 10}
                                },
                           "Legolas":
                               {"raza": "Elfo",
                                "faccion": "La comunidad del anillo",
                                "ubicacion": "Bosque Negro",
                                "equipamiento": {"nombre": "Arco de Galadriel", "tipo": "Arco","potencia": 70},
                                "relaciones": {"personaje": "Aragorn", "tipo": "Amigo", "nivel_confianza": 10}
                                },
                           "Gimli":
                               {"raza": "Enano",
                                "faccion": "La comunidad del anillo",
                                "ubicacion": "Rivendel",
                                "equipamiento": {"nombre": "Hacha de Gimli", "tipo": "Hacha","potencia": 75},
                                "relaciones": {"personaje": "Aragorn", "tipo": "Amigo", "nivel_confianza": 9}
                                },
                           "Frodo":
                               {"raza": "Hobbit",
                                "faccion": "La comunidad del anillo",
                                "ubicacion": "Hobbiton",
                                "equipamiento": {"nombre": "Daga de Frodo", "tipo": "Daga","potencia": 40},
                                "relaciones": {"personaje": "Boromir", "tipo": "Neutral", "nivel_confianza": 5}
                                },
                           "Boromir":
                               {"raza": "Humano",
                                "faccion": "La comunidad del anillo",
                                "ubicacion": "Rivendel",
                                "equipamiento": {"nombre": "Espada de Boromir", "tipo": "Espada", "potencia": 70},
                                "relaciones": {"personaje": "Frodo", "tipo": "Neutral", "nivel_confianza": 5}
                                },
                           "Saruman":
                               {"raza": "Humano",
                                "faccion": "Isengard",
                                "ubicacion": "Isengard",
                                "equipamiento": {"nombre": "Báculo de Saruman", "tipo": "Bastón","potencia": 90},
                                "relaciones": {"personaje": "Galadriel", "tipo": "Enemigo", "nivel_confianza": 2}
                                },
                           "Galadriel":
                               {"raza": "Elfo",
                                "faccion": "Lothlórien",
                                "ubicacion": "Bosque Negro",
                                "equipamiento": {"nombre": "Arco de Galadriel", "tipo": "Arco","potencia": 70},
                                "relaciones": {"personaje": "Saruman", "tipo": "Enemigo", "nivel_confianza": 2}
                                },
                           "Sauron":
                               {"raza": "Humano",
                                "faccion": "Mordor",
                                "ubicacion": "Mordor",
                                "equipamiento": {"nombre": "Anillo Único", "tipo": "Objeto especial","potencia": 100},
                                "relaciones": {"personaje": "Aragorn", "tipo": "Enemigo", "nivel_confianza": 1}
                                }
                           }

def add_character():

    nombre = input(
        "Introduce el nombre del personaje: (Aragorn, Legolas, Gimli, Frodo, Boromir, Saruman, Galadriel, Sauron): ").lower().capitalize()

    if nombre not in personajes_disponibles:
        raise Exception("El nombre introducido no es valido.")
    
    else: 

        characters[nombre] = {
            "raza": detalles_personajes[nombre]["raza"],
            "faccion": detalles_personajes[nombre]["faccion"],
            "ubicacion": detalles_personajes[nombre]["ubicacion"],
            "equipamiento": {
                "nombre": detalles_personajes[nombre]["equipamiento"]["nombre"],
                "tipo": detalles_personajes[nombre]["equipamiento"]["tipo"],
                "potencia": detalles_personajes[nombre]["equipamiento"]["potencia"],
                             },
            "relaciones": {
                "personaje": detalles_personajes[nombre]["relaciones"]["personaje"], 
                "tipo": detalles_personajes[nombre]["relaciones"]["tipo"],
                "nivel_confianza": detalles_personajes[nombre]["relaciones"]["nivel_confianza"]
                        }
        }

def show_characters_per_faction(faction):
    if not characters:
         print(f"No hay ningún personaje en el sistema. ")
         return

    for nombre, detalles in characters.items():
        if detalles["faccion"] == faction:
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

def show_characters_per_equipment(equipment):
    if not characters:
         print(f"No hay ningún personaje en el sistema. ")
         return

    for nombre, detalles in characters.items():
        if detalles["equipamiento"]["nombre"] == equipment:
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


def show_characters():

    if not characters: 
         print(f"No hay ningún personaje en el sistema. ")
         return
    
    for nombre, detalles in characters.items():
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
    show_characters()
    show_characters_per_faction("Mordor")
    show_characters_per_equipment("Ardúril")

if __name__ == "__main__":
    main()
