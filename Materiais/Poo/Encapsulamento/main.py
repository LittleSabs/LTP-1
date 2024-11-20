from Paciente import Paciente

paciente1 = Paciente('Vanessa',
                     41,
                     '56432187321')
paciente1.nome = 'Rodrigo'
print(paciente1.nome)

paciente1.setIdade(-3)
print(paciente1.getIdade())

paciente1.cpf = '456'
print(paciente1.cpf)
paciente1._idade = 12
print(paciente1._idade)
paciente1.__cpf = '31465489456'
print(paciente1.__cpf)
paciente1._Paciente__cpf = 4
print(paciente1._Paciente__cpf)