# Funções padrões
def título(txt):
    print(f'\033[1;34;40m{txt}\033[m')

def linhasimples(cor, tamanho):
    print(f'\033[{cor}m-\033[m' * tamanho)

def linhadupla(cor, tamanho):
    print(f'\033[{cor}m-=\033[m' * tamanho)


# Importação de bibliotecas


# Título do programa
título('ficha do jogador')

# Objetos


# Funções
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} no campeonato.')



# Lógica
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
