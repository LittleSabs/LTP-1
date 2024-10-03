from pyexpat.errors import messages
 
 
def saudacao():
    print('Hello World')
saudacao()
 
def saudacao2(nome):
    print('Hello ', nome)
saudacao2('Ana')
 
def soma(a,b):
    print(a+b)
soma(3,2)
 
def mensagem(nome = "Pedro", mensagem = 'Olá'):
    print(nome, mensagem)
mensagem()
mensagem('Ana')
mensagem('Ana', 'Tudo Bem?')
 
def subtracao(a,b):
    return a-b
resultado = subtracao(3,2)
print(resultado)
 
def cadastro(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave} : {valor}')
cadastro(nome='Pedro', idade = 45, endereço = 'Rua 40',sobrenome = 'Silva')
 
def media(*numeros):
    print(sum(numeros)/len(numeros))
media(1,2,3,4,5,10,56,32,78,23)
