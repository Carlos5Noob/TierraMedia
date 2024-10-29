from features.characters.characters import characters

different_locations = {}

locations = ("Rivendel", "Hobbiton", "Minas Tirith", "Mordor", "Isengard", "Bosque Negro", "Lothlórien")

def change_location(ch_name):
    character = characters.get(ch_name.capitalize())
    print(f"La ubicación actual de este personaje es {character['ubicacion']}")
    local = input(f"¿A qué ubicación desea cambiarlo?: ")
    character["ubicacion"] = local
    while character["ubicacion"].lower() not in locations.lower():
        input(f"{character['ubicacion']} es una región desconocida de este reino, inténtelo de nuevo")
    return

    change_location()