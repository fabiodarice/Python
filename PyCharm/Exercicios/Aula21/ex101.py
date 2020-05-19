# Funções padrões
def título(txt):
    print(f'\033[1;34;40m{txt.upper()}\033[m')

def linhasimples(cor, tamanho):
    print(f'\033[{cor}m-\033[m' * tamanho)

def linhadupla(cor, tamanho):
    print(f'\033[{cor}m-=\033[m' * tamanho)


# Importação de bibliotecas
from datetime import date

# Título do programa
título('funções para votação')

# Objetos


# Funções
def voto(nasc):
    anos = date.today().year - nasc
    if anos < 18:
        return f'Com {anos} anos: NÃO VOTA'
    elif 18 <= anos <= 65:
        return f'Com {anos} anos: VOTO OBRIGATÓRIO'
    elif anos > 65:
        return f'Com {anos} anos: VOTO OPCIONAL'


# Lógica
linhasimples(33, 40)
n = int(input('Em que ano você nasceu? '))
resp = voto(n)
print(resp)
