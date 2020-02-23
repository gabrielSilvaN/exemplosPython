#Importando o módulo json
import json

#Abrindo o arquivo no modo read (somente leitura)
arquivo = open('arquivo.txt', 'r')

#Lendo as linhas do arquivo (é perfeitamente possível fazer arquivo.open('arquivo.txt', 'r').readlines()
linhas = arquivo.readlines()

#Loop para iterar nas linhas do arquivo
for i in linhas:

    #Convertendo cada linha codificada em json para um dict (para confirmar basta fazer print(type(user))
    user = json.loads(i)

    nome = user['Nome']
    #print(nome)

    idade = user['Idade']
    #print(idade)

    sexo = user['Sexo']
    #print(sexo)    

    #'Descomente' alguma das linhas abaixo para debug:
    #print(type(user))
    #print(user.keys())
    #print(user.values())
    
    

arquivo.close()




