# Importação de bibliotecas
dados = list()

# Título do programa
print('\033[1;34;40mAPRIMORANDO OS DICIONÁRIOS\033[m')

# Objetos
while True:
    jogador = {'Nome':str(input('Nome do Jogador: ')).strip().capitalize(), 'gols':[], 'total':0}

    # Lógica
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    for c in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))
        jogador['total'] += jogador['gols'][c]

    dados.append(jogador.copy())
    jogador.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

    print('-' * 40)

print('\033[34m-=\033[m' * 40)

print(f'{"cod":<5}{"nome":<10}{"gols":<20}{"total":>10}')
print('-' * 50)
for n, info in enumerate(dados):
    print(f'{n:<5}{info["Nome"]:<10}{str(info["gols"]):<20}{info["total"]:>10}')

print('\033[34m-=\033[m' * 40)

while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 interrompe): '))

    if mostrar == 999:
        break

    while mostrar >= len(dados):
        print('Valor inválido. ', end='')
        mostrar = int(input('Mostrar dados de qual jogador? (999 interrompe): '))

    print(f'-- LEVANTAMENTO DO JOGADOR {dados[mostrar]["Nome"]}:')


    for n, info in enumerate(dados[mostrar]['gols']):
        print(f'No jogo {n + 1} fez {info} gols.')


    print('-' * 30)

print('<< VOLTE SEMPRE >>')