
numeros = [1,2,3,4]

soma = (lambda x,y: x+y)


resultado = reduce(soma, numeros)

print(resultado)