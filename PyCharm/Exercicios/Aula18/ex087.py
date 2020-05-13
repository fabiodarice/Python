# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mMAIS SOBRE MATRIZ EM PYTHON\033[m')

# Objetos
matriz = [[], [], [], [], [], [], [], [], []]
pares = 0
maior = 0

# Lógica
'''Coleta os dados de entrada e separa por lista'''
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

'''Mostra das listas em forma de matriz 3 x 3'''
for num, dados in enumerate(matriz):
    if num < 3:
        print(f'[{dados[0]:^5}]', '', end='')
print()
for num, dados in enumerate(matriz):
    if 3 <= num < 6:
        print(f'[{dados[0]:^5}]', '', end='')
        if dados[0] > maior:
            maior = dados[0]
print()
for num, dados in enumerate(matriz):
    if 6 <= num < 9:
        print(f'[{dados[0]:^5}]', '', end='')
print()

print('=-' * 30)

'''Determina quais são os valores pares de todas as listas e soma-os'''
for dados in matriz:
    if dados[0] % 2 == 0:
        pares += dados[0]

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {matriz[2][0] + matriz[5][0] + matriz[8][0]}')
print(f'O maior valor da segunda coluna é {maior}')