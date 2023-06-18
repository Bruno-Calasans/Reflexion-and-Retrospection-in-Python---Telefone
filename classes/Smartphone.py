from TelefoneMovel import TelefoneMovel

class Smartfone(TelefoneMovel):
    def __init__(self, marca, modelo, valor):
        TelefoneMovel.__init__(self, marca, modelo, valor, 'Smartfone')
        