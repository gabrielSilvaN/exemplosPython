funcaoChamada = False

def function():
    #usamos a variável do contexto global
    global funcaoChamada
    funcaoChamada = True

function()

print(funcaoChamada)
