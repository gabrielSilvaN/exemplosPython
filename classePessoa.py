class Pessoa(object):

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def falar(self):
        print('Oi, me chamo %s e tenho %d anos de idade' %(self.nome, self.idade))
        
