class Livro:
    def __init__(self,titulo,autor,ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
 
    def getTitulo(self):
        return self.__titulo
 
    def setTitulo(self,novoTitulo):
        self.__titulo = novoTitulo
 
    @property
    def autor(self):
        return self.__autor
 
    @property
    def ano(self):
        return self.__ano
   
    @ano.setter
    def ano(self, novoAno):
        self.__ano = novoAno
 
livro1 = Livro('As Duas Torres','Tolkien',1954)
print(livro1.getTitulo())
print(livro1.autor)
livro1.ano = 1955