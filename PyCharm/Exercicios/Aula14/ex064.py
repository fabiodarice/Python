# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mSOMA DE VÁRIOS NÚMEROS\033[m')

# Objetos
num = 0
digitados = 0
soma = 0

# Lógica
while num != 999:
    num = int(input('\033[30mDigite um valor qualquer para somar ou 999 para encerrar o programa:\033[m '))
    if num != 999:
        digitados += 1
        soma += num
print('A quantidade de números digitados foi \033[4;33m{}\033[m e a soma entre eles foi \033[4;34m{}\033[m'.format(digitados, soma))