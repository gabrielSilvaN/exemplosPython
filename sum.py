numeros = [1,2,3,4]

# Ao invés de iterar a lista de números e somá-los como a seguir:

def func(*numeros):
    soma = 0
    for i in numeros:
        soma+=i
    return soma

#print("A soma dos números é %.2f: "%func(1,2,3,4,5))

# Podemos simplesmente usar sum(), onde é recebido uma lista de números como argumento
print("A soma dos números é %.2f" %sum(numeros))
