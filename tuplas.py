#isso é uma tupla em python

a = (1,2,3)

#print(a)

#print(type(a))

#isso também é uma tupla em python

b = 1,2

#print(b)
#print(type(b))

#tuplas são imutáveis

c = 1,2,3

#print(c[0])

#c[0] = 3 #gera um erro

#fazer swap (troca de valores) de variáveis usando tuplas é muito mais simples

a = 3

b = 7

#print(a,b)

#criando uma tupla com elementos que já existem
tupla = (a,b)

#print(tupla)

#fazendo um swap de a e b com os elementos da tupla
b,a = tupla

#print(a,b)

#é possível fazer comparações com tuplas ( <,>,<=,>=,==,!=) obtendo um booleano como resposta

a = (1,2,3)
b = (5,6,7)

#print(a < b)

#é possível atribuir valores
email = 'gabriel_silva@discente.ufg.br'
user, domain = email.split('@')

print(domain)
