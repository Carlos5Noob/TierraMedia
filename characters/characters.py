characters = {}

personajes_disponibles = ["Aragorn", "Legolas", "Gimli", "Frodo", "Boromir", "Saruman", "Galadriel", "Sauron"]
detalles_personajes = {"Aragorn":
                               {"raza": "Humano",
                                "faccion": "La comunidad del anillo",
                                "ubicacion": "Rivendel"
                                },
                           "Legolas":
                               {"raza": "Elfo",
                                "faccion": "La comunidad del anillo",
                                "ubicacion": "Bosque Negro"
                                },
                           "Gimli":
                               {"raza": "Enano",
                                "faccion": "La comunidad del anillo",
                                "ubicacion": "Rivendel"
                                },
                           "Frodo":
                               {"raza": "Hobbit",
                                "faccion": "La comunidad del anillo",
                                "ubicacion": "Hobbiton"
                                },
                           "Boromir":
                               {"raza": "Humano",
                                "faccion": "La comunidad del anillo",
                                "ubicacion": "Rivendel"
                                },
                           "Saruman":
                               {"raza": "Humano",
                                "faccion": "Isengard",
                                "ubicacion": "Isengard"
                                },
                           "Galadriel":
                               {"raza": "Elfo",
                                "faccion": "Lothlórien",
                                "ubicacion": "Bosque Negro"
                                },
                           "Sauron":
                               {"raza": "Humano",
                                "faccion": "Mordor",
                                "ubicacion": "Mordor"
                                }
                           }

def add_character():
    nombre = input(
        "Introduce el nombre del personaje: (Aragorn, Legolas, Gimli, Frodo, Boromir, Saruman, Galadriel, Sauron)").capitalize()
    if nombre not in personajes_disponibles:
        raise Exception("El nombre introducido no es valido.")

    characters[nombre] = {
        "raza": detalles_personajes[nombre]["raza"],
        "faccion": detalles_personajes[nombre]["faccion"],
        "ubicacion": detalles_personajes[nombre]["ubicacion"]
    }
