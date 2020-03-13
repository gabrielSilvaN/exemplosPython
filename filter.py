from random import randint

numeros = []
pares = (lambda a: a % 2 == 0)

# coloando numeros aleatorios na lista
for i in range(0,100):
    numeros.append(randint(0,100))


resultado = filter(pares, numeros)

print(resultado)


