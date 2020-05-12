# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mEXTRAINDO DADOS DE UMA LISTA\033[m')

# Objetos
lista = []

# Lógica
while True:
    lista.append(int(input('Digite um valor: ')))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
lista.sort(reverse=True)

print('-=' * 30)

print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
print(f'{"O valor 5 faz parte da lista" if 5 in lista else "O valor 5 não foi encontrado na lista"}')
