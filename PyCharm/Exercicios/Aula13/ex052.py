# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mVERIFICAÇÃO DE NÚMERO PRIMO\033[m')

# Objetos
n = int(input('\033[30mDigite um número:\033[m '))
s = 0

# Lógica
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        s = s + 1
    else:
        print('\033[30m', end=' ')
    print('{}'.format(c), end=' ')
if s == 2:
    print('\n\033[mEste número \033[4;34mé primo!!!\033[m')
else:
    print('\n\033[mEste número \033[1;31mNÃO é primo!!!\033[m')
