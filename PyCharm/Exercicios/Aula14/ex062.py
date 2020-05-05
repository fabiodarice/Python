# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mPROGRESSÃO ARITMÉTIVA COM QUANTIDADE DE TERMOS DEFINIDA PELO USUÁRIO\033[m')

# Objetos
termos = 0
vezes = 10

n = int(input('\033[30mDigite o número do primeiro termo:\033[m '))
r = int(input('\033[mDigite a razão da P.A.:\033[m '))

# Lógica
while vezes != 0:
    while termos != vezes:
        print('\033[{}m{}\033[m'.format(30 + termos, n), end=' ')
        termos = termos + 1
        n = n + r
    vezes = int(input('\n\033[30mDeseja mostrar mais quantos termos?:\033[m '))
    termos = 0
print('\033[33mFIM!\033[m')