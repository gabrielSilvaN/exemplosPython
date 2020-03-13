numeros = [1,2,3,4]
duplica = (lambda a : 2*a)


# def duplica(a):
#     return 2*a

# func = duplica

resultado = map(duplica,numeros)

# print(type(resultado))

pessoas = [{"Nome": "Gabriel", "Idade": 23}, {"Nome": "Isabella", "Idade": 20}, {"Nome": "Kaio", "Idade": 22}]
pegaNomes = (lambda a : a["Nome"])


listaNomes = map(pegaNomes, pessoas)
print(listaNomes)