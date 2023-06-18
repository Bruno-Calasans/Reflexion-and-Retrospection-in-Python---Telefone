class TelefoneMovel:
    def __init__(self, marca, modelo, valor, tipo='Celular'):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.valor = valor

    def impInfos(self):
        c = self.__class__.__name__
        infos = "\nv---------- %s ----------v\n%s\n%s\n%.2f" %(c, self.marca, self.modelo, self.valor)
        print(infos)

    def setMarca(self, umaMarca):
        self.marca = umaMarca
    def setModelo(self, umModelo):
        self.modelo = umModelo
    def setValor(self, umValor):
        self.valor = umValor