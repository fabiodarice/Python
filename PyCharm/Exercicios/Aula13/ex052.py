# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mVERIFICAÇÃO DE NÚMERO PRIMO\033[m')

# Objetos
n = int(input('\033[30mDigite um número:\033[m '))
s = n
v = 0

# Lógica
for c in range(n, 0, -1):
    s = s - 1
    if s != 0:
        if s != 1 and n % s == 0:
            v = 1
if v == 1:
    print('Este número \033[1;31mNÃO é primo!!!\033[m')
else:
    print('Este número \033[4;34mé primo!!!\033[m')
