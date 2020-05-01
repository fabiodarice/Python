# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mSOMA ÍMPARES MÚLTIPLOS DE TRÊS\033[m')

# Objetos
s = 0

# Lógica
for c in range(1, 500, 2):
    if c % 3 == 0:
        s = s + c
print('A somatória de todos os números ímpares múltiplos de 3 entre 1 e 500 é \033[4;34m{}\033[m'.format(s))