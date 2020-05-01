# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mSOMATÓRIA DE 6 NÚMEROS INTEIROS PARES\033[m')

# Objetos
s = 0

# Lógica
for c in range(0, 6):
    n = int(input('\033[30mDigite um número:\033[m '))
    if n % 2 == 0:
        s += n
print('A somatória dos números pares digitados é \033[4;34m{}\033[m'.format(s))