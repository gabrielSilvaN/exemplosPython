#sum por padrão não aceita números passados como argumentos, mas se usarmos
#parametros variáveis (*args) e os espalharmos, é possível utilizá-los em sum
def sumAll(*args):
    return sum(args)


print(sumAll(3,2,1,5,6))


