# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mVERIFICAÇÃO DE PESO\033[m')

# Objetos
menor = 0
maior = 0

# Lógica
for c in range(0, 5):
    peso = float(input('\033[30mDigite o peso kg:\033[m '))
    if peso > maior:
        maior = peso
    if menor == 0 or peso < menor:
        menor = peso
print('O menor peso foi \033[4;34m{}\033[m e o maior peso foi \033[4;34m{}\033[m'.format(menor, maior))