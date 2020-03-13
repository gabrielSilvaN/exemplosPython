from dependente import *

class Pessoa(object):
    def __init__(self,nome,idade,peso, dependente):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.dependente = dependente

    def msg(self):
        print("Oi, estou falando. Me chamo",self.nome);


pessoa = Dependente("Joãozinho", "Estudante")
gabriel = Pessoa('Gabriel', 23, 50.4,pessoa)
gabriel.msg()
gabriel.dependente.falar()
