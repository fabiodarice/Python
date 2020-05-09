# Importação de bibliotecas
from random import randint

# Título do programa
print('\033[1;34;40mMAIOR E MENOR VALORES EM TUPLA\033[m')

# Objetos


# Lógica
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram:', '', end='')

for c in range(0, 5):
    print(n[c], '', end='')

print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O manor valor sorteado foi {min(n)}')