import turtle
import turtle as t

class forma:
    def desenhar(self):
        t.forward(100)
        turtle.done()

class circulo(forma):
    def desenhar(self):
        t.circle(30)
        turtle.done()

class quadrado(forma):
    def desenhar(self):
        for _ in range(4):
            t.forward(100)
            t.right(90)
        turtle.done()

#circulo= circulo()
#circulo.desenhar()

quadrado= quadrado()
quadrado.desenhar()