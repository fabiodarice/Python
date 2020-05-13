# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mMAIS SOBRE MATRIZ EM PYTHON\033[m')

# Objetos
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Lógica
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()