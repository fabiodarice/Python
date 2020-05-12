# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mMAIOR E MENOR VALORES NA LISTA\033[m')

# Objetos
valores = list()

# Lógica
for c in range(0, 5):
    valores.append(int(input(f'\033[30mDigite um valor para a Posição {c}:\033[m ')))

maior = max(valores)
menor = min(valores)

print('=-' * 30)

print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, num in enumerate(valores):
    if maior == num:
        print(f'{pos}...', '', end='')

print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for pos, num in enumerate(valores):
    if menor == num:
        print(f'{pos}...', '', end='')
