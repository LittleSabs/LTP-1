# Abrindo e fechando um arquivo manualmente
file = open('exemplo.txt', 'w')  # Abrindo para escrita
file.write('Primeira linha do arquivo.\n')
file.close()  # Fechando o arquivo

#'r': leitura (padrão).
#'w': escrita (substitui o conteúdo, ou cria o arquivo se não existir).
#'a': adição de conteúdo ao final do arquivo.
#'b': modo binário, geralmente usado para arquivos não-textuais.

# Usando 'with' para garantir que o arquivo será fechado automaticamente
with open('exemplo.txt', 'a') as file:
  # 'a' de append para adicionar texto
  file.write('Segunda linha do arquivo.\n')

  # Lê o arquivo inteiro
with open('exemplo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)

# Lê linha por linha
from time import sleep
with open('exemplo.txt', 'r') as file:
  for linha in file:
    print(linha.strip())
    sleep(1)
    # strip() remove espaços em branco no início e fim da linha

# Lê linha por linha em forma de lista
with open('exemplo.txt', 'r') as file:
    linhas = file.readlines()  # Retorna uma lista de linhas
    print(linhas)

# Lê o arquivo inteiro
with open('entrada.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)

# Contando palavras em um arquivo
with open('entrada.txt', 'r') as file:
    conteudo = file.read().lower()
    palavras = conteudo.split()

contador_palavras = {} #{'palavra': quantidade}
for palavra in palavras:
    if palavra in contador_palavras:
        contador_palavras[palavra] += 1
    else:
        contador_palavras[palavra] = 1

# Escrevendo o resultado em um arquivo
with open('contagem_palavras.txt', 'w') as file:
    for palavra, contagem in contador_palavras.items():
        file.write(f'{palavra}: {contagem}\n')

# Trabalhando com arquivos csv
import csv #comma separated values

dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Ana', '22', 'São Paulo'],
    ['João', '35', 'Rio de Janeiro']
]

with open('saida.csv', 'w', newline='') as file:
    escritor = csv.writer(file)
    escritor.writerows(dados)

with open('winequality-red.csv', 'r') as file:
    leitor = csv.reader(file)
    for linha in leitor:
        print(linha)