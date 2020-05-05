# Importação de bibliotecas
from random import randint

# Título do programa
print('\033[1;34;40mADIVINHAÇÃO\033[m')

# Objetos
palpites = 0
acertou = False

# Lógica
print('\033[34m-=-\033[m' * 30)
print('Tente adivinhar o número escolhido pelo computador que será entre 0 e 5')
print('\033[34m-=-\033[m' * 30)

computador = randint(0, 10)

while not acertou:
    usuario = int(input('\033[30mDigite um número entre 0 e 10:\033[m '))
    if usuario == computador:
        acertou = True
    if usuario < computador:
        print('\033[1;31mMais\033[m, tente mais uma vez')
    if usuario > computador:
        print('\033[1;31mMenos, tente mais uma vez')
    palpites = palpites + 1
print('Parabéns você \033[4;34mACERTOU!\033[m, foram necessários {} palpites'.format(palpites))