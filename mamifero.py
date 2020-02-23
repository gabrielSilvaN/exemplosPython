class Mamifero(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return 'Olá, me chamo %s e tenho %d anos'%(self.nome, self.idade)


class Humano(Mamifero):
    def __init__(self, nome, idade, cor):
        super(nome,idade)
        self.cor = cor


gabriel = Humano('Gabriel', 23, 'Branco')
    
