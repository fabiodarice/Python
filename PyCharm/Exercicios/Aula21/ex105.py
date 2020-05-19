# Funções padrões
def título(txt):
    print(f'\033[1;34;40m{txt.upper()}\033[m')


def linhasimples(cor, tamanho):
    print(f'\033[{cor}m-\033[m' * tamanho)


def linhadupla(cor, tamanho):
    print(f'\033[{cor}m-=\033[m' * tamanho)


# Importação de bibliotecas


# Título do programa
título('analisando e gerando dicionários')

# Objetos


# Funções
def notas(*valor, sit=False):
    maior = menor = total = media = 0
    situacao = ''
    for num in valor:
        if num > maior:
            maior = num
        if menor == 0 or num < menor:
            menor = num
        total += 1
        media += num
    media = media / total
    if media < 5:
        situacao = 'RUIM'
    elif 5 <= media < 7:
        situacao = 'RAZOÁVEL'
    elif media >= 7:
        situacao = 'BOA'
    if sit == False:
        return {'total':total, 'maior':maior, 'menor':menor, 'média':media}
    else:
        return {'total':total, 'maior':maior, 'menor':menor, 'média':media, 'situação':situacao}



# Lógica
resp = notas(8.5, 7.8, 9.2, sit=False)
print(resp)