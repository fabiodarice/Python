# Importação de bibliotecas


# Título do programa
print('\033[mPROGRESSÃO ARITMÉTICA\033[m')

# Objetos
n = int(input('\033[30mDigite o número do primeiro termo:\033[m '))
r = int(input('\033[30mDigite a razão da P.A.:\033[m '))
cor = 0

# Lógica
for c in range(n, (10 * r) + 1, r):
    cor += 1
    print('\033[33m', c, '\033[m')