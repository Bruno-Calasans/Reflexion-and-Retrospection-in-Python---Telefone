from TelefoneMovel import TelefoneMovel

class Celular(TelefoneMovel):
    def __init__(self, marca, modelo, valor):
        self.tipo = 'Celular'
        TelefoneMovel.__init__(self, marca, modelo, valor)