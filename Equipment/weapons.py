from pyexpat.errors import messages

weapons = {}

weapon = ['Espada Andúril', 'Arco de Galadriel', 'Hacha de Gimli', 'Daga de Frodo', 'Báculo de Saruman', 'Anillo Único',
           'Espada de Boromir']

type_weapon = ['Espada', 'Arco', 'Hacha', 'Daga', 'Baston', 'Anillo']

armors = ['Cota de malla', 'Cota de espinas', 'Armadura de oro', 'Capa del hechicero', 'Armadura del héroe',
          'Manto élfico', 'Armadura quebrada']

weapon_power = {
    weapon[0]: 100, weapon[1]: 60, weapon[2]: 80, weapon[3]: 70,  weapon[4]: 80, weapon[5]: 60, weapon[6]: 50
}

def show_weapons():

    if not weapon:
        message = f"No weapons found"
        return message
    else:
        print(weapon)


