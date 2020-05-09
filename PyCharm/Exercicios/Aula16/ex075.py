# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mANÁLISE DE DADOS EM UMA TUPLA\033[m')

# Objetos


# Lógica
v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
v3 = int(input('Digite mais um número: '))
v4 = int(input('Digite o último número: '))

números = (v1, v2, v3, v4)

print(f'Você digitou os valores {números}')

print(f'O valor 9 apareceu {números.count(9)} vezes')

if 3 in números:
    print(f'O valor 3 apareceu na {números.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram', '', end='')
for c in range(0, 4):
    if números[c] % 2 == 0:
        print(números[c], '', end='')

