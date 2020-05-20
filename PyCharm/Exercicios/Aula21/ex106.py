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
opção = ' '

# Funções
def ajuda(txt):
    linha('~', 33, 30)
    print(f'\033[30;44mAcessando o manual do comando {txt}\033[m')
    sleep(1)
    linha('~', 33, 30)
    print('\033[7;30m')
    help(txt)
    print('\033[m')
    linha('~', 33, 30)


# Lógica
linha('~', 33, 30)
print('\033[30;42mSISTEMA DE AJUDA PyHelp\033[m')
linha('~', 33, 30)
while True:
    opção = str(input('\033[7;31mFunção ou Biblioteca >\033[m ')).strip().lower()
    if opção == 'fim':
        break
    ajuda(opção)
linha('~', 33, 30)
print('\033[30;46mATÉ LOGO!\033[m')
linha('~', 33, 30)
