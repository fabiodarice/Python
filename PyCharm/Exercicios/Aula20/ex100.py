# Importação de bibliotecas
from random import randint
from time import sleep

# Título do programa
print('\033[1;34;40mFUNÇÕES PARA SORTEAR E SOMAR\033[m')

# Objetos
números = list()

# Funções
def sorteia():
    for n in range(0, 5):
        números.append(randint(1, 10))

def somapar():
    soma = 0
    for n, info in enumerate(números):
        if info % 2 == 0:
            soma += info
    print(soma)


# Lógica
sorteia()
print(f'Sorteando 5 valores da lista: ', end='')
for n, info in enumerate(números):
        print(info, '', end='')
        sleep(0.5)
print('PRONTO!')
print(f'Somando os valores pares de {números}, temos ', end='')
somapar()