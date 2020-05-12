# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mVALORES ÚNICOS EM UMA LISTA\033[m')

# Objetos
valores = list()


# Lógica
while True:
    n = int(input('\033[30mDigite um valor:\033[m '))
    if n not in valores:
        valores.append(n)
        print('\033[1;34mValor adicionado com sucesso...\033[m')
    else:
        print('\033[1;31mValor duplicado! Não vou adicionar...\033[m')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\033[30mQuer continuar: [S/N]\033[m ')).strip().upper()
    if continuar == 'N':
        break
valores.sort()
print('-=' * 30)
print(f'Você digitou os valores {valores}')