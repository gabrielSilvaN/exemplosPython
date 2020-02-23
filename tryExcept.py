#tenta exceutar o que está dentro do try, se der erro, aprensenta o except

try:
    arquivo = open('arquivo2')
except:
    print('Desculpe, algo deu errado')
