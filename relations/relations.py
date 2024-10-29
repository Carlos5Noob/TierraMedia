from characters.characters import characters

personajes_disponibles = ["Aragorn", "Legolas", "Gimli", "Frodo", "Boromir", "Saruman", "Galadriel", "Sauron"]

def add_relationship(name):
    nombre_relacion = input(f"Introduzca el nombre del personaje con el que va a tener relación con {name}")
    while nombre_relacion not in personajes_disponibles:
        nombre_relacion = input("El personaje seleccionado no existe. Inténtelo de nuevo: \n ")

    tipo = input("Introduce el tipo de relación: ")
    nivel_confianza = int(input("Introduce el nivel de confianza: "))

    character_relation = characters.get(name)