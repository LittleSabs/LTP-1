semana = ('domingo','segunda','terça','quarta','quinta','sexta','sabado')
#semana = ('domingo',30,'terça',False,'quinta',3.14,'sabado')
#semana = 'domingo','segunda','terça','quarta','quinta','sexta','sabado'
 
print(semana)
print(semana[3])
print(semana[-2])
print(len(semana))
print(semana.index('quinta'))
print(semana.count('sexta'))
 
idades = (21,56,2,87,102,13,45)
 
print(max(idades))
print(min(idades))
print(sum(idades))
media = sum(idades)/len(idades)
print('A média é {:.2f}'.format(media))
