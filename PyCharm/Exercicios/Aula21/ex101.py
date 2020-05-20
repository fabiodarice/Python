# Funções padrões
def título(txt):
    print(f'\033[1;34;40m{txt.upper()}\033[m')

def linha(tipo, cor, tamanho):
    print(f'\033[{cor}m{tipo}\033[m' * tamanho)


# Importação de bibliotecas
from datetime import date

# Título do programa
título('funções para votação')

# Objetos


# Funções
def voto(nasc):
    idade = date.today().year - nasc
    if idade < 18:
        msg = f'Com {idade} anos: NÃO VOTA.'
    elif 18 <= idade < 65:
        msg = f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade > 65:
        msg = f'Com {idade} anos: VOTO OPCIONAL.'
    return msg


# Lógica
linha('~', 33, 30)
print(voto(int(input('Em que ano você nasceu? '))))


