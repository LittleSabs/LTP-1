class Cor():
    def __init__(self,R,G,B):
        self.R = R
        self.G = G
        self.B = B
 
    def getColor(self):
        return (self.R/255,
                self.G/255,
                self.B/255)
     
import turtle as tl
from CorClass import Cor
cor1 = Cor(3, 248, 252)
tl.color(cor1.getColor())
tl.forward(100)
tl.done()