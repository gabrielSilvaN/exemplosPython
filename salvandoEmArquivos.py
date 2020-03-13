#Importando o módulo json 
import json

#Abrindo o arquivo no módulo append (adicionar uma nova linha ao fim do documento)
arquivo = open("arquivo.txt", "a", encoding='utf-8')

#Lendo 2 usuários
for i in range(2):

    #Leitura dos dados
    nome = input("Digite seu nome:")
    idade = input('Digite sua idade:')
    sexo = input('Digite seu sexo:')

    #Gerando um dicionário com os dados lidos
    myDict = {'Nome' : nome, 'Idade' : idade, 'Sexo' : sexo}

    #Convertendo o dicionário para o formato Json
    myDictJson = json.dumps(myDict)

    #Gravando o Json no arquivo
    arquivo.write(myDictJson + '\n')

#Fechando o arquivo
arquivo.close()
