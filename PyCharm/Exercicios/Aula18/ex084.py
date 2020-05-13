# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mLISTA COMPOSTA E ANÁLISE DE DADOS\033[m')

# Objetos
dados = list()
pessoas = list()
pesado = 0.0
leve = 0.0


# Lógica
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

for info in pessoas:
    if info[1] > pesado:
        pesado = info[1]
    if leve == 0.0 or info[1] < leve:
        leve = info[1]

print('=-' * 30)

print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {pesado:.1f}Kg. Peso de ', end='')
for info in pessoas:
    if info[1] == pesado:
        print(f'[{info[0]}]', '', end='')
print()
print(f'O menor peso foi {leve:.1f}Kg. Peso de ', end='')
for info in pessoas:
    if info[1] == leve:
        print(f'[{info[0]}]', '', end='')
