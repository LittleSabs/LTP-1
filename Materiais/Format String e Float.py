nome = 'Pedro'
idade = 30
 
print('O seu nome é',nome,'e sua idade é',idade)
print('O seu nome é'+nome+'e sua idade é'+str(idade))
 
print('O seu nome é {} e sua idade é {} anos.'.format(nome,idade))
print('O seu nome é {0} e sua idade é {1} anos.'.format(nome,idade))
 
print(f'O seu nome é {nome} e sua idade é {idade} anos.')
 
altura = 1.7583146878
peso = 78.5489745612
 
print('Sua altura é {:.2f} e seu peso é {:.1f}.'.format(altura,peso))
print('Sua altura é {} e seu peso é {}.'.format(
round(altura),
    round(peso)))
print(f'Sua altura é {altura:.2f} e seu peso é {peso:.1f}.')
