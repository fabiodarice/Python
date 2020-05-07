# Importação de bibliotecas
from random import randint

# Título do programa
print('\033[1;34;40mJOGO DO PAR OU ÍMPAR\033[m')

# Objetos
qtd = 0

# Lógica
print('\033[33m=-\033[m' * 25)
print('\033[1;34mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('\033[33m=-\033[m' * 25)

while True:
    computador = randint(0, 10)

    jogador = int(input('\033[30mDiga um valor:\033[m '))
    seleção = str(input('\033[30mPar ou Ímpar? [P/I]:\033[m ')).strip().upper()
    soma = computador + jogador
    parouimpar = 'PAR' if soma % 2 ==0 else 'IMPAR'

    print('\033[34m-\033[m' * 50)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {parouimpar}')
    print('\033[34m-\033[m' * 50)

    if seleção == 'P' and soma % 2 == 0 or seleção == 'I' and soma % 2 != 0:
        print('Você VENCEU!\nVamos jogar novamente...')
        print('\033[33m=-\033[m' * 25)
        qtd += 1
    elif seleção == 'P' and soma % 2 != 0 or seleção == 'I' and soma % 2 == 0:
        print('Você PERDEU!')
        break

print('\033[33m=-\033[m' * 25)
print(f'GAME OVER! Você venceu \033[4;34m{qtd}\033[m vezes')
