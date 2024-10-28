import random

def fight(fighter1, fighter2):
    healing_before_battle(fighter1)
    healing_before_battle(fighter2)
    print(f"Empieza el combate entre {fighter1.name} y {fighter2.name}")
    while fighter1.hp > 0 and fighter2.hp > 0:
        print(f"Turno de {fighter1.name}")

        if fighter1.attack(check_prob(fighter1)):
            print(f"El ataque ha acertado, le has causado daños por valor de {fighter1.weapon_power}PV")
            fighter2.hp -= fighter1.weapon_power
        else:
            print(f"El ataque ha fallado, mala suerte!")

        print(f"Turno de {fighter2.name}")

        if fighter2.attack(check_prob(fighter2)):
            print(f"El ataque ha acertado, le has causado daños por valor de {fighter2.weapon_power}PV")
            fighter1.hp -= fighter2.weapon_power
        else:
            print(f"El ataque ha fallado, mala suerte!")

    if fighter1.hp <= 0:
        print(f"{fighter1.name} ha perdido este combate")
    if fighter2.hp <= 0:
        print(f"{fighter2.name} ha perdido este combate")

def healing_before_battle(fighter):
    fighter.hp = 300

def attack(chance):

    if chance >= random.randint(1, 100):
        return True
    else:
        return False

def check_prob (weapon):
    attack_chance = 0

    if "espada" in weapon.lower():
        attack_chance= 50
    if "daga" in weapon.lower():
        attack_chance= 40
    if "hacha" in weapon.lower():
        attack_chance= 45
    if "arco" in weapon.lower():
        attack_chance= 65
    if "baston" in weapon.lower():
        attack_chance= 60
    if "anillo" in weapon.lower():
        attack_chance= 70

    return attack_chance
