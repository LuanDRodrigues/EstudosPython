import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão Falhou!!!\nErro: {}'.format(e))
        sys.exit()
    print('Socket criado com sucesso!!')

    hostAlvo = input('Digite o Host a ser concetado: ')
    portaAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print('Cliente TCP Conectado Com Sucesso')
        print('Host: {} \nPorta: {}'.format(hostAlvo, portaAlvo))
        s.shutdown(2)
    except socket.error as e:
        print('A conexão falhou!!')
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ == '__main__':
    main()