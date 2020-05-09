# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mTUPLAS COM TIMES DE FUTEBOL\033[m')

# Objetos
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

# Lógica
print('\033[33m-=\033[m' * 30)
print(f'Lista de Times do Brasileirão: {times}')
print('\033[33m-=\033[m' * 30)
print(f'Os 5 primeiros são {times[:5]}')
print('\033[33m-=\033[m' * 30)
print(f'Os 4 últimos são {times[-4:]}')
print('\033[33m-=\033[m' * 30)
print(f'Times em ordem alfábetica: {sorted(times)}')
print('\033[33m-=\033[m' * 30)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')