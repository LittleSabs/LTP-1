class Paciente:
    # self:construtor, passa as informações para ele mesmo
    def __init__(self, nome, idade, cpf):
        #public
        self.nome= nome
        #protected
        self._idade= idade
        #private(+forte)
        #self.cpf= cpf
        #public
        self.__cpf= cpf

    def getIdade(self):
        return self._idade

    def setIdade(self, idade):
        if idade > 0:
            self._idade=idade
        else:
            print("Nova idade inválida")

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf= cpf


        '''
        public string nome
        protected int idade
        prvate String cpf
        '''
