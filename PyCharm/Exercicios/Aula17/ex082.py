# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mDIVIDINDO VALORES EM VÁRIAS LISTAS\033[m')

# Objetos
valores = list()
pares = list()
impares = list()

# Lógica
while True:
    valores.append(int(input('\033[30mDigite um valor:\033[m ')))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        pares.append(valores[c])
    else:
        impares.append(valores[c])
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
