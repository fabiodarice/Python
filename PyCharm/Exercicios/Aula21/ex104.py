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
    while True:
        numero = str(input(txt))
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
    return numero


# Lógica
linhasimples(33, 40)

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')