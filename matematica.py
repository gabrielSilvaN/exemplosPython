"""Essa classe oferece métodos customizados para efetuar operações matemáticas"""
class Matematica(object):

    #Este método retorna a soma de a com b
    def sum(a,b):
        return a+b;    

    #Este método retorna a diferenca de a por b
    def sub(a,b):
        return a-b    

    #Este método retorna o produto a por b
    def mult(a,b):
        return a*b    

    #Este método retorna o quociente de a por b
    def div(a,b):
        if b!=0:
            return a/b
        else:
            return 'Impossível dividir por zero'
        
    #Este método retorna o resultado de a elevado a b
    def exp(a,b):
        if b==0:
            return 1
        elif b<0:
            return 1/(a**(-b))
        else:
            return a**b
        
    #Este método retorna o maior dentre dois números
    def inv(a):
        return -a

    #Este método retorna o maior dentre dois números
    def maior(a,b):
        if a > b :
            return a
        return b

    #Este método retorna o menor dentre dois números
    def menor(a,b):
        if a < b:
            return a
        return b

    #Este método calcula a raiz quadrada de um número
    def raiz2(a):
        if a >= 0:
            return a**(1/2)
        return 'Impossível calcular raíz quadrada de número negativo'

    #Este método calcula a raiz n-ésima de um número
    def raizN(a,b):
        if a >= 0:
            return a**(1/b)
        return 'Impossível calcular raíz quadrada de número negativo'
        
