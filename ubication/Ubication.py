class Ubication:
    def __init__(self, tipo):
        self.tipo = tipo

    @property
    def tipo(self):
        return self.tipo

    @tipo.setter
    def tipo(self, tipo):
        self.tipo = tipo