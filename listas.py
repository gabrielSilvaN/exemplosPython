#isso é uma lista em python
lista = [1,2,3]

#print(lista)

#podemos colocar qualquer tipo de dado em uma lista, inclusive misturá-los

lista = ['Palavra', 'Teste', 2.0, 3, [1,2,3,4], ()]

print(lista[0][3])

#tamanho de uma lista:

print(len(lista))

#tamanho de um item da lista:

print(len(lista[0]))


#juntando elementos de lista com elementos de uma tupla

s = 'abc'
l = [1,2,3]
listaPares = []

for i in zip(s,l):
    print(i)
    listaPares.append(i)

print(listaPares)

