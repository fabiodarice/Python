# Importação de bibliotecas


# Título do programa
print('\033[mPROGRESSÃO ARITMÉTICA\033[m')

# Objetos
n = int(input('\033[30mDigite o número do primeiro termo:\033[m '))
r = int(input('\033[30mDigite a razão da P.A.:\033[m '))
cor = 29

# Lógica
for c in range(n, (n + (10 - 1) * r) + r, r):
    cor = cor + 1
    print('\033[{}m'.format(cor), c, '\033[m')