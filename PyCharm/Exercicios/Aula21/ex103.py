# Funções padrões
def título(txt):
    print(f'\033[1;34;40m{txt}\033[m')

def linha(tipo, cor, tamanho):
    print(f'\033[{cor}m{tipo}\033[m' * tamanho)


# Importação de bibliotecas


# Título do programa
título('ficha do jogador')

# Objetos


# Funções
def ficha(j='<desconhecido>', g=0):
    return f'O jogador {j} fez {g} gols no campeonato.'


# Lógica
linha('-', 34, 40)
jogador = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Número de gols: ')).strip()

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador == '':
    print(ficha(g=gols))
else:
    print(ficha(jogador, gols))
