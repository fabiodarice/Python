# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mPROGRESSÃO ARITMÉTIVA DOS 10 PRIMEIROS TERMOS COM "WHILE"\033[m')

# Objetos
vezes = 0

n = int(input('\033[30mDigite o número do primeiro termo:\033[m '))
r = int(input('\033[mDigite a razão da P.A.:\033[m '))

# Lógica
while vezes != 10:
    print('\033[{}m{}\033[m'.format(30 + vezes, n), end=' ')
    vezes = vezes + 1
    n = n + r
