#Exemplo que mostra algo como operador ternário presente em C, Js, etc
#Em C seria algo do tip a%2 == 0 ? 'Par' : 'Ímpar'
def parImpar(a):
    return 'Par' if a%2 == 0 else 'Ímpar'

print(parImpar(2))
