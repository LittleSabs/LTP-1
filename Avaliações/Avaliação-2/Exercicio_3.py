import turtle as t

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def desenhar_ponto(ponto):
    t.goto(ponto.x, ponto.y)

x = float(input("Informe a coordenada x: "))
y = float(input("Informe a coordenada y: "))

ponto1 = Ponto(x, y)

desenhar_ponto(ponto1)
t.penup()
desenhar_ponto(ponto1)
t.dot(5, 'pink')
t.pendown()
t.done()

#professor, ele vai abrir uma nova aba, mas n vai para ela automaticamnete. o senhor tem que abrir ela, muito obrigada