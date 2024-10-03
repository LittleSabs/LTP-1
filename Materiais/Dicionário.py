'''
cliente = {}
cliente = dict(id = 0,nome = 'Pedro',mensalidade = 249.99,
              ativo = True,altura = 1.78,peso = 86)
chaves = ['id','nome','mensalidade','ativo','altura','peso']
cliente = dict.fromkeys(chaves, 0)
'''
cliente = {
    'id':0,
    'nome':'Pedro',
    'mensalidade':249.99,
    'ativo':True,
    'altura':1.78,
    'peso':86
}
print(cliente['nome'])
print(cliente.get('nome'))
 
print(cliente.items())
for chave, valor in cliente.items():
    print(f'{chave} : {valor}')
 
print(cliente.keys())
for chave in cliente.keys():
    print(chave)
 
print(cliente.values())
for valor in cliente.values():
    print(valor)
 
cliente.update({'ativo': False})
cliente.update({'endereço': 'Quadra 2'})
print(cliente)
 
print(cliente.setdefault('peso'))
print(cliente.setdefault('treinador','Nulo'))
print(cliente)
 
endereco = cliente.pop('endereço')
print(endereco)
ultimo = cliente.popitem()
print(ultimo)
print(cliente)
 
print(len(cliente))
cliente2 = cliente.copy()
cliente.clear()
print(cliente)
print(cliente2)
