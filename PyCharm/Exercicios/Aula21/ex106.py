# Funções padrões
def título(txt):
    print(f'\033[1;34;40m{txt.upper()}\033[m')


def linha(tipo, cor, tamanho):
    print(f'\033[{cor}m{tipo}\033[m' * tamanho)



# Importação de bibliotecas
from time import sleep

# Título do programa
título('sistema interativo de ajuda do python')

# Objetos


# Funções
def ajuda(txt):
    return f'Acessando o manual do comando {txt}'
    sleep(1)
    return help(txt)


# Lógica
linha('~', 33, 40)
título('sistema de ajuda pyhelp')
linha('~', 33, 40)
result = ajuda(str(input('Função ou Biblioteca > ')))
print(result)