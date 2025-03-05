from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('ESCOLHA ENTRE:\n[0]Pedra\n[1]Papel\n[2]Tesoura')

jogador = int(input('QUAL SUA ESCOLHA ?: '))
print('CARREGANDO...')
sleep(2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-='*15)
print(f'Você Escolheu: {(itens[jogador])}')
print(f'Computador Escolheu: {(itens[computador])}')
print('-='*15)

if computador == 0:

    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('\033[1;32mVOCÊ GANHOU\033[m')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR GANHOU\033[m')
    else:
        print('TENTATIVA INVALIDA!!!')

elif computador == 1:

        if jogador == 1:
            print('EMPATE')
        elif jogador == 0:
            print('\033[1;31mCOMPUTADOR GANHOU\033[m')
        elif jogador == 2:
            print('\033[1;32mVOCÊ GANHOU\033[m')
        else:
            print('TENTATIVA INVALIDA!!!')

elif computador == 2:

            if jogador == 2:
                print('EMPATE')
            elif jogador == 0:
                print('\033[1;32mVOCÊ GANHOU\033[m')
            elif jogador == 1:
                print('\033[1;31mCOMPUTADOR GANHOU\033[m')
            else:
                print('TENTATIVA INVALIDA!!!')