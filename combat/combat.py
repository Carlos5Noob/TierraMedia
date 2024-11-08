from time import sleep
from random import randint, random

class Combat:
    def __init__(self):
        pass

    def fight(self, ft1, ft2):
        """
        Inicia un combate entre dos personajes.
        """
        print("Has elegido la opción de combate entre dos personajes.")
        print("Aquí tienes una lista de todos los personajes:\n")

        if not ft1 or not ft2:
            print("Uno o ambos personajes no existen.")
            return

        self.healing_before_battle(ft1)
        self.healing_before_battle(ft2)

        print(f"Empieza el combate entre {ft1['nombre']} y {ft2['nombre']}")

        while ft1["hp"] > 0 and ft2["hp"] > 0:
            print(f"\nTurno de {ft1['nombre']}")

            if "equipamiento" not in ft1:
                print(f"{ft1['nombre']} no tiene un arma equipada y huye del combate.")
                break

            if "equipamiento" not in ft2:
                print(f"{ft2['nombre']} no tiene un arma equipada y huye del combate.")
                break

            sleep(0.75)

            if self.attack(self.check_prob(ft1["equipamiento"]["nombre"])):
                print(f"El ataque ha acertado, {ft1['nombre']} ha causado {ft1['equipamiento']['daño']} puntos de daño.")
                ft2["hp"] -= ft1["equipamiento"]["daño"]
            else:
                print(f"El ataque de {ft1['nombre']} ha fallado.")

            sleep(1.5)

            if ft2["hp"] <= 0:
                print(f"{ft2['nombre']} ha perdido este combate.")
                break

            sleep(1)

            print(f"\nTurno de {ft2['nombre']}")
            sleep(0.75)

            if self.attack(self.check_prob(ft2["equipamiento"]["nombre"])):
                print(f"El ataque ha acertado, {ft2['nombre']} ha causado {ft2['equipamiento']['daño']} puntos de daño.")
                ft1["hp"] -= ft2["equipamiento"]["daño"]
            else:
                print(f"El ataque de {ft2['nombre']} ha fallado.")

            sleep(1.5)

            if ft1["hp"] <= 0:
                print(f"{ft1['nombre']} ha perdido este combate.")
                break

            sleep(1.5)

    def healing_before_battle(self, fighter):
        """Restaura los puntos de salud del luchador a 300 antes de la batalla."""
        fighter["hp"] = 300

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
