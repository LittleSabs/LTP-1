class Paciente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome #public
        self._idade = idade #protected
        self.__cpf = cpf #private (+forte)

    def getIdade(self):
        return self._idade

    def setIdade(self, idade):
        if idade > 0:
            self._idade = idade
        else:
            print('Nova Idade Inválida')

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf