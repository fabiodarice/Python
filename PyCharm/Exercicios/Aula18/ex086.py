# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mMATRIZ EM PYTHON\033[m')

# Objetos
matriz = [[], [], [], [], [], [], [], [], []]

# Lógica
for c in range(0, 9):
    if c < 3:
        n = int(input(f'Digite um valor para [0, {c}]: '))
        matriz[c].append(n)
    elif 3 <= c < 6:
        n = int(input(f'Digite um valor para [1, {c - 3}]: '))
        matriz[c].append(n)
    elif 6 <= c < 9:
        n = int(input(f'Digite um valor para [2, {c - 6}]: '))
        matriz[c].append(n)

print('=-' * 30)

for num, dados in enumerate(matriz):
    if num < 3:
        print(f'[{dados[0]:^5}]', '', end='')
print()
for num, dados in enumerate(matriz):
    if 3 <= num < 6:
        print(f'[{dados[0]:^5}]', '', end='')
print()
for num, dados in enumerate(matriz):
    if 6 <= num < 9:
        print(f'[{dados[0]:^5}]', '', end='')

