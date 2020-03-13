#from matematica import *

#print(Matematica.exp(1,-2))
#print(Matematica.div(2,0))
#print(Matematica.menor(3,4))
#print(Matematica.inv(3))
#print(Matematica.raiz2(-3)) #raiz2 é o mesmo que raiz quadrada
#print(Matematica.raizN(8,3))

arquivo = open('./classePessoa.py', 'r')
linhas = arquivo.readlines()

for i in linhas:
    print(i)
