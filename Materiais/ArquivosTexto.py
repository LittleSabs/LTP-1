#abrir e fechar arquivo manualmente
from os import write

file= open('exemplo.txt', 'w') #abrindo pra escrita
file.write('Primeira linha do arquivo. \n')
file.close() #fechando arquivo
''''
'r': leitura (padrao)
'w': escrita (substitui o conteudo ou cria o arquivo se nao existir
'a': adição de conteudo ao final do arquivo
'b': modo binario, geralmente usado para arquivos não-textuais
'''
#usando with para garantir que o arquivo seraz fechado automaticamente
with open('exemplo.txt', 'a') as file:
    #a de append para adicionar no texto
    file.write('Segunda linha do arquivo')

#le o arquivo inteiro
with open('exemplo.txt', 'r') as file:
    conteudo=file.read()
    print(conteudo)

#le linha por linha
from time import sleep
with open('exemplo.txt', 'r') as file:
    for linha in file:
        print(linha.strip())
        sleep(1)
        #strip() remove espaços em branco no inicio e fim da linha

#contando palavras em um arquivo
with open('exemplo.txt', 'r') as file:
    conteudo=file.read().lower()
    palavras=conteudo.split()

contador_palavras={} #{'palavra: quantidade}
for palavra in palavras:
    if palavra in contador_palavras:
        contador_palavras[palavra] += 1
    else:
        contador_palavras[palavra] = 1

#escrevendo o resultaod em arquivo
with open('exemplo.txt', 'w') as file:
    for palavra, contagem in contador_palavras.items():
        file.write(f"{palavra}: {contagem}\n")

#Trabalhando com arquivos csv
import csv #comma separated values
dados= [
    ['nome', 'idade', 'cidade']
    ['ana', '22', 'Sao paulo']
    ['joao','35','Rio de Janeiro']
]
with open('exemplo.csv', 'w', newline='') as file:
    escritor = csv.writer(file)
    escritor.writerows(dados)