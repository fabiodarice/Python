# Importação de bibliotecas


# Título do programa
print('\033[mTABUADA\033[m')

# Objetos
n = int(input('\033[30mDigite um valor inteiro:\033[m '))

# Lógica
print('\033[31m-\033[m' * 12)
for c in range(0, 10):
    print('\033[{}m{} x {:2} = {}\033[m'.format(30 + c, n, c, n *c))
print('\033[31m-\033[m' * 12)