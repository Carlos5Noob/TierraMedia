def show_menu():

    continuar = True
    opcion = 0
    while continuar:
        print("""----- Menu Juego Tierra Media -----
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

        try:
            while opcion <=0 or opcion >10:
                print("Introduzca un número del 1 al 10")
                opcion = int(input())
        except ValueError:
                print("Opcion no válida, introduzca un número")

        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                continuar = False
                return print(f"Saliendo del programa...")


show_menu()