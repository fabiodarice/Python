# Importação de bibliotecas
from random import randint
from time import sleep

# Título do programa
print('\033[1;34;40mFUNÇÕES PARA SORTEAR E SOMAR\033[m')

# Objetos
números = list()

# Funções
def sorteia(lista):
    for n in range(0, 5):
        lista.append(randint(1, 10))
        print(n, '', end='')
        sleep(0.5)
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {números}, temos {soma}', end='')


# Lógica
sorteia(números)
somapar(números)