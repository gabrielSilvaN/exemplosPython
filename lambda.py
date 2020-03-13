#coding: utf-8
#em python é possível atribuir uma função à uma variável

def soma(a,b,c):
    return a+b+c

a = soma

# print(a(1,2,3))


#com as funções lambda, obtemos uma sintaxe mais enxuta:

f = (lambda a,b,c,d: a+b+c+d)

print(f(1,2,3,4))