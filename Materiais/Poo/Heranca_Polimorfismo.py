class Inimigo():
    def __init__(self,nome, hp, dano):
        self.nome = nome
        self.hp = hp
        self.dano = dano
 
    def emitirSom(self):
        print('Inimigo', self.nome)
 
    def receberDano(self,dano):
        self.hp -= dano
        print('HP:',self.hp)
        if self.hp <= 0:
            print('Morreu')
 
class Lobo(Inimigo):
    def __init__(self,nome, hp, dano,escudo):
        super().__init__(nome,hp,dano)
        self.escudo = escudo
 
    def emitirSom(self):
        super().emitirSom()
        print('Auuuuuuuuuuuuuuuu!')
 
    def receberDano(self,dano):
        danoFinal = dano - self.escudo
        if danoFinal > 0:
            super().receberDano(danoFinal)
 
lobo1 = Lobo('Lobo Mal',
            50,
            50,
            50)
lobo1.emitirSom()
lobo1.receberDano(60)
lobo1.receberDano(80)
lobo1.receberDano(60)
 