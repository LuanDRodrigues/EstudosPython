import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket Criado com Sucesso!')

host = 'localhost'
porta = 5432

s.bind((host, porta))
mensagem = ('Servidor: Olá Cliente, Pode falar!')

while True:
    dados, end = s.recvfrom(4096)
    pass

    if dados:
        print('Servidor Enviando Mensagem !!!')
        s.sendto(dados + (mensagem.enconde()), end)


