from xmlrpc.client import boolean


class Equipment():

    def __init__(self, equipment_name, equipment_type, equipment_power):
        self.equipment_name = equipment_name
        self.equipment_type = equipment_type
        self.equipment_power = equipment_power

    @property
    def equipment_name(self):
        return self.equipment_name

    @equipment_name.setter
    def equipment_name(self, equipment_name):
        if isinstance(equipment_name, str):
            self.equipment_name = equipment_name
        else:
            raise ValueError('El nombre del equipamiento debe ser una cadena de carácteres: ')

    @property
    def equipment_type(self):
        return self.equipment_type

    @equipment_type.setter
    def equipment_type(self, equipment_type):
        if isinstance(equipment_type, str):
            self.equipment_type = equipment_type
        else:
            raise ValueError('El tipo de equipamiento debe ser una cadena de carácteres: ')

    @property
    def equipment_power(self):
        return self.equipment_power

    @equipment_power.setter
    def equipment_power(self, equipment_power):
        if isinstance(equipment_power, int):
            self.equipment_power = equipment_power
        else:
            raise ValueError('El poder del arma debe ser una cadena numérica: ')

    def is_a_weapon(self, equipment_type):
        if isinstance(equipment_type, Equipment):
            return True
        else:
            return False
