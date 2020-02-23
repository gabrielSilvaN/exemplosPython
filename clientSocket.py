# coding: utf-8

import socket as s

socket_c = s.socket()

ponto = ("localhost", 3000)

socket_c.connect(ponto)


while True:

    msg = input('>>')
    if msg != 'quit':
        socket_c.send(msg.encode())
    else:
        socket_c.send(msg.encode())
        print('Fechando conexão com o servidor')
        break;

    resposta = socket_c.recv(1024).decode()
    print(resposta)
