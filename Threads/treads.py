from threading import Thread
from time import sleep

# Corrida com carros e velocidade definidas.
def carro1(velocidade):
    trajeto = 0

    while trajeto <= 100:
        print('Carro 1:', trajeto)
        trajeto += velocidade

def carro2(velocidade):
    trajeto = 0

    while trajeto <= 100:
        print('Carro 2:', trajeto)
        trajeto += velocidade


# Corrida com Input pelo usuário.
def carro(velocidade, piloto):
    msg = str()
    trajeto = 0
    itera = 0
    pista = 100

    while trajeto <= pista:
        itera += 1
        trajeto += velocidade
        sleep(1) 
        print('Piloto {:<10} {:^5} km/s - {:>8} km '.format(piloto, velocidade, trajeto))
    sleep(3)
    msg = 'O piloto',piloto,' finalizou a corrida em',itera,' segundos.'
    return msg
    



if __name__ == '__main__':
    print('==  DISPUTANDO CORRIDA  ==') 
    resp = []
    dic = dict()
    msg = str()
    cond = 0
    count = 0

    while True:
        piloto = (str(input('Digite o nome do Piloto: ')))
        vel = (int(input(f'Qual a velocidade do {piloto}: ')))

        dic[piloto] = vel

        cond = int(input('[1] Iniciar a corrida\n[2] Adicionar Piloto\n[3] Sair:\n'))
        if cond == 3:
            break

        # Iniciar corrida
        elif cond == 1:
            count = 0
            print('Corrida iniciada')
            print(dic)

            # Repete a estrutura de dicionário!!
            for k,v in dic.items():
                t_carro = Thread(target= carro, args=[v, k])
                t_carro.start()
                resp.append(msg)
                print(resp)
            pass
                
        # Adicionar Piloto
        elif cond == 2:
            pass

    #carro1(15)
    #carro2(20)