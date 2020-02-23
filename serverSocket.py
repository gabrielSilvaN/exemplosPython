# coding: utf-8

import socket as s

#criando o objeto socket para o servidor
socket_s = s.socket()

#pontos da conexão(host e porta). Deve ser uma tupla
ponto = ("localhost", 3000)

#fazendo o bind do ponto à conexão
socket_s.bind(ponto)

#fazer o servidor escutar por conexões. O número no parâmetro indica
#o máximo de conexões esperadas ao mesmo tempo
socket_s.listen(1)

#socket_c, (host_c, porta_c) = socket_s.accept()

sc, addr = socket_s.accept()
print("Conexão estabelecida com ", addr)

while True:    
    recibido = sc.recv(1024).decode()
    if recibido == "quit":
        break
    print("Recibido:", recibido)
    msg = input('>>')
    sc.send(msg.encode())

print("fechando servidor")
sc.close()
socket_s.close()

