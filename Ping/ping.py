import os
from time import sleep

def pingSimples():
        # comment: 
    # end def
    arquivo = open("Ping/filename.txt", 'w')
    ip_host = input('Digite IP ou Host: ')
    texto = str(os.system('ping -n 6 {}'.format(ip_host)))
    arquivo.write(texto)
    arquivo.close()

def pingMultiplo():
    with open('Ping/hosts.txt') as file:
        dump = file.read().splitlines()
        print(dump)

        for ip in dump:
            print(os.system('ping -n 6 {}'.format(ip)))
            sleep(5)


if __name__ == '__main__':
    p = int(input('[ 1 ] Ping Simples [ 2 ] Ping Multiplo'))

    if p == 1:
        pingSimples()
    elif p == 2:
        pingMultiplo()
    else:
        print('Escolha um valor válido')
