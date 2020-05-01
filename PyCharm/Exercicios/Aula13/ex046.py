# Importação de bibliotecas
from time import sleep
from emoji import emojize

# Título do programa
print('\033[1;34;40mCONTAGEM REGRESSIVA FOGOS DE ARTIFÍCIO\033[m')

# Objetos


# Lógica
for c in range(10, 0, -1):
    print('\033[{}m'.format(40 - c), c, '\033[m')
    sleep(1)
print(emojize(':fireworks:' * 20, use_aliases=True))