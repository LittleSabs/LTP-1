class Carro():
    def __init__(self,marca, modelo, cor, ano,quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.quilometragem = quilometragem
 
    def acelerar(self):
        print('Vrooom!')
 
    def frenar(self):
        print('Carro parando')
 
    def getModelo(self):
        return self.modelo
 
    def getCor(self):
        return self.cor
 
    def setCor(self, novaCor):
        self.cor = novaCor
