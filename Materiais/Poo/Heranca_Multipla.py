class NPC:
    def __init__(self,nome, gold):
        self.nome = nome
        self.gold = gold
 
    def falar(self):
        print('Olá, bem-vindo!')
 
class Inimigo():
    def __init__(self,nome,hp, dano):
        self.nome = nome
        self.hp = hp
        self.dano = dano
 
    def falar(self):
        print('MORRAAAAA!')
 
class Personagem(NPC,Inimigo):
    def __init__(self,nome,gold,hp, dano):
        NPC.__init__(self,nome,gold)
        Inimigo.__init__(self,nome,hp,dano)
 
    def falar(self):
        #super().falar()
        NPC.falar(self)
        Inimigo.falar(self)
 
personagem1 = Personagem('Patches',521,100,20)
print(personagem1.nome)
print(personagem1.hp)
personagem1.falar()
#personagem1.NPC.falar()
print(Personagem.mro())