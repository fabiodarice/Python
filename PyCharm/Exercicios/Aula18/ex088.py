# Importação de bibliotecas
from random import randint
from time import sleep

# Título do programa
print('\033[1;34;40mPALPITES PARA A MEGA SENA\033[m')

# Objetos
jogos = list()
temp = list()
diferente = False

# Lógica
print('-' * 50)
print(f'{"JOGA NA MEGA SENA":^50}')
print('-' * 50)

qtdjogos = int(input('Quantos jogos você quer que eu sorteie? '))

print('-=' * 3, f'SORTEANDO {qtdjogos} JOGOS', '-=' * 3)
for c in range(1, qtdjogos + 1):
    for d in range(1, 7):
        numero = randint(0, 60)
        if numero not in temp:
            temp.append(numero)
        else:
            while True:
                numero = randint(0, 60)
                if numero not in temp:
                    temp.append(numero)
                    break

    temp.sort()
    jogos.append(temp[:])
    temp.clear()

    print(f'Jogo {c}: {jogos[c - 1]}')
    sleep(1)

print(f'{" < BOA SORTE! > ":~^50}')