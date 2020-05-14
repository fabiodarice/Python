# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mCADASTRO DE JOGADOR DE FUTEBOL\033[m')

# Objetos
jogador = {'Nome':str(input('Nome do Jogador: ')).strip().capitalize(), 'gols':[], 'total':0}

# Lógica
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for c in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['total'] += jogador['gols'][c]

print('\033[34m-=\033[m' * 40)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('\033[34m-=\033[m' * 40)

print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na partida {c + 1}, fez {jogador["gols"][c]} gols.')

print(f'Foi um total de {jogador["total"]} gols')
