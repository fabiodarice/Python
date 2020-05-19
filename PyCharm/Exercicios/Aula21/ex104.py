# Funções padrões
def título(txt):
    print(f'\033[1;34;40m{txt.upper()}\033[m')

def linhasimples(cor, tamanho):
    print(f'\033[{cor}m-\033[m' * tamanho)

def linhadupla(cor, tamanho):
    print(f'\033[{cor}m-=\033[m' * tamanho)


# Importação de bibliotecas


# Título do programa
título('validando entrada de dados do python')

# Objetos


# Funções
def leiaInt(txt):
    numero = str(input(txt))
    if numero.isnumeric():
        numero = int(numero)
        return numero
    else:
        return 'doido'


# Lógica
linhasimples(33, 40)

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')