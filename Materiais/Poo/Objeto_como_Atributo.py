class Autor:
    def __init__(self,nome,pais,nascimento):
        self.nome = nome
        self.pais = pais
        self.nascimento = nascimento
 
    def autorInfo(self):
        print(f'Autor: {self.nome},'
              f'País: {self.pais},'
              f'Ano Nascimento: {self.nascimento}')
 
class Livro:
    def __init__(self,titulo,ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
 
    def livroInfo(self):
        print(f'Titulo: {self.titulo},'
              f'Ano de Publicação: {self.ano},'
              f'Autor: {self.autor.nome}')
 
autor1 = Autor('Tolkien','Inglaterra',
               1892)
livro1 = Livro('As Duas Torres', 1954, autor1)
livro1.livroInfo()
livro1.autor.autorInfo()