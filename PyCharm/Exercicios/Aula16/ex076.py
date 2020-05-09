# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mLISTA DE PREÇOS COM TUPLA\033[m')

# Objetos
lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
n = 0

# Lógica
print('\033[34m-\033[m' * 50)
print(f'\033[33m{"LISTAGEM DE PREÇOS":^50}\033[m')
print('\033[34m-\033[m' * 50)

while True:

    print(lista[n]+ '.' * (48 - (len(lista[n]) + 7)), end='')
    n += 1
    print(f'R${lista[n]:>7.2f}')
    n += 1

    if len(lista) == n:
        break
print('\033[34m-\033[m' * 50)