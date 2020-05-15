# Importação de bibliotecas
from random import randint
from time import sleep
from operator import itemgetter

# Título do programa
print('\033[1;34;40mJOGO DE DADOS EM PYTHON\033[m')

# Objetos
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
             'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
cont = 1

# Lógica
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)

print(f'{"Ranking dos jogadores":+^30}')

for k, v in sorted(jogadores.items(), key=itemgetter(1), reverse=True):
    print(f'{cont}° lugar: {k} com {v}')
    cont += 1
    sleep(1)