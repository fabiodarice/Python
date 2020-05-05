# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mFATORIAL\033[m')

# Objetos


# Lógica
n = int(input('Digite um número inteiro: '))
fatorial = resultado = n
if n != 0:
    while n != 1:
        n = n -1
        resultado = resultado * (n)
    print('\033[33m{}!\033[m = \033[34m{}\033[m'.format(fatorial, resultado))
else:
    print('\033[33m{}!\033[m = \033[34m1\033[m'.format(fatorial))
