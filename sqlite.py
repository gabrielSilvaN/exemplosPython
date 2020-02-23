#Importando o módulo do sqlite3
import sqlite3

#Criando uma conexão com o banco de dados
conn = sqlite3.connect("Teste.db")

#Cursor é o responsável por executar ações no banco
cursor = conn.cursor()

#executando um select no banco de dados
cursor.execute("SELECT * FROM Funcionario;")

#cursor.execute("INSERT INTO Funcionario VALUES('Lucas', 17);")

#fecthone obtém somente um resultado do select, é útil quando fazemos
#consultas que retornam apenas um resultado
#print(cursor.fetchone())

#fecthall obtém todos os resultados e os salva em uma lista
#cada elemento da lista é uma tupla
print(cursor.fetchall())


#Fazendo o autocommit das ações realizadas no banco
conn.commit()


#Fechando a conexão
conn.close()
