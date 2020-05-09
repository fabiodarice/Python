# Importação de bibliotecas
from random import randint

# Título do programa
print('\033[1;34;40mMAIOR E MENOR VALORES EM TUPLA\033[m')

# Objetos
maior = 0
menor = 0

# Lógica
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram:', '', end='')

for c in range(0, 5):

    print(n[c], '', end='')

    if n[c] > maior:
        maior = n[c]

    if menor == 0 or n[c] < menor:
        menor = n[c]

print(f'\nO maior valor sorteado foi {maior}')
print(f'O manor valor sorteado foi {menor}')