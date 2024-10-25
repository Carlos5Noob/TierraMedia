import random
from random import Random

def fight(fighter1, fighter2):
    healing_before_battle(fighter1)
    healing_before_battle(fighter2)
    print(f"Empieza el combate entre {fighter1.name} y {fighter2.name}")


def healing_before_battle(fighter):
    fighter.hp = 300

def attack(chance):

    if chance >= random.randint(1, 100):
        return True;
    else:
        return False;

def check_prob (weapon):
    attack_chance = 0

    if weapon.lower() == "espada":
        attack_chance= 50
    if weapon.lower() == "daga":
        attack_chance= 40
    if weapon.lower() == "hacha":
        attack_chance= 45
    if weapon.lower() == "arco":
        attack_chance= 65
    if weapon.lower() == "baston":
        attack_chance= 60
    if weapon.lower() == "anillo":
        attack_chance= 70

    return attack_chance
