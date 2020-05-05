# Importação de bibliotecas
from random import randint
from time import sleep

# Título do programa
print('\033[1;34;40mADIVINHAÇÃO\033[m')

# Objetos
usuario = 6
computador = 6
palpites = 1

# Lógica
print('\033[34m-=-\033[m' * 30)
print('Tente adivinhar o número escolhido pelo computador que será entre 0 e 5')
print('\033[34m-=-\033[m' * 30)

computador = randint(0, 5)

while usuario != computador:
    usuario = int(input('\033[30mDigite um número entre 0 e 5:\033[m '))
    print('\033[33mPROCESSANDO...\033[m')
    sleep(1)
    if usuario != computador:
        print('Você \033[1;31mERROU\033[m, continue tentando!')
        palpites = palpites + 1
print('Parabéns você \033[4;34mACERTOU!\033[m, foram necessários {} palpites'.format(palpites))