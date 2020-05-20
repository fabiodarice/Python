# Funções padrões
def título(txt):
    print(f'\033[1;34;40m{txt.upper()}\033[m')


def linha(tipo, cor, tamanho):
    print(f'\033[{cor}m{tipo}\033[m' * tamanho)


# Importação de bibliotecas


# Título do programa
título('analisando e gerando dicionários')

# Objetos


# Funções
def notas(*valor, sit=False):
    dic = {}
    dic['total'] = len(valor)
    dic['maior'] = max(valor)
    dic['menor'] = min(valor)
    dic['média'] = sum(valor) / len(valor)
    if sit == True:
        if dic['média'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['média'] >= 5:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'RUIM'
    return dic


# Lógica
resp = notas(8.5, 7.8, 9.2, sit=True)
print(resp)
