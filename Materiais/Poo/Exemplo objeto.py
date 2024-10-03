from carroClass import Carro
 
carro1 = Carro('Toyota',
               'Corolla',
               'azul',
               2017,
               30000)
carro1.acelerar()
carro1.frenar()
print(carro1.getModelo())
carro1.setCor('branco')
print(carro1.getCor())
carro2 = Carro('Chevrolet',
               'Onix',
               'preto',
               2020,
               100000)
carro2.acelerar()
print(carro2.getModelo())
