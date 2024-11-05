import time
import random

class Combat:
    def __init__(self):
        def fight(ft1, ft2):
            """
            Inicia un combate entre dos personajes.
            """
            print("Has elegido la opción de combate entre dos personajes. ")
            print("Aquí tienes una lista de todos los personajes: \n")

            if not ft1 or not ft2:
                print("Uno o ambos personajes no existen.")
                return

            healing_before_battle(ft1)
            healing_before_battle(ft2)

            print(f"Empieza el combate entre {ft1.nombre} y {ft2.nombre}")

            while ft1.hp > 0 and ft2.hp > 0:
                print(f"\nTurno de {ft1.nombre}")

                if "equipment" not in ft1:
                    print(
                        f"{ft1.nombre} no tiene un arma equipada y no puede atacar, por lo tanto huye del combate.")
                    break
                if "equipment" not in ft2.nombre:
                    print(
                        f"{ft2.nombre} no tiene un arma equipada y no puede atacar, por lo tanto huye del combate.")
                    break
                time.sleep(0.75)
                if attack(check_prob(ft1.equipamiento["nombre"])):
                    print(
                        f"El ataque ha acertado, {ft1.nombre} ha causado {ft1.equipamiento["daño"]} puntos de daño.")
                    ft2.hp -= ft1.equipamiento["daño"]
                else:
                    print(f"El ataque de {ft1.nombre} ha fallado, mala suerte!")

                time.sleep(1.5)

                if ft2.hp <= 0:
                    print(f"{ft2.nombre} ha perdido este combate")
                    break

                time.sleep(1)

                print(f"\nTurno de {ft2.nombre}")

                time.sleep(0.75)

                if attack(check_prob(ft2.equipamiento["nombre"])):
                    print(
                        f"El ataque ha acertado, {ft2.nombre} ha causado {ft2.equipamiento["daño"]} puntos de daño.")
                    ft1.hp -= ft2.equipamiento["daño"]
                else:
                    print(f"El ataque de {ft2.nombre} ha fallado, mala suerte!")

                time.sleep(1.5)

                if ft1.hp <= 0:
                    print(f"{ft1.nombre} ha perdido este combate")
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
