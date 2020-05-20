# Funções padrões
def título(txt):
    print(f'\033[1;34;40m{txt}\033[m')

def linha(tipo, cor, tamanho):
    print(f'\033[{cor}m{tipo}\033[m' * tamanho)


# Importação de bibliotecas


# Título do programa
título('função para fatorial')

# Objetos


# Funções
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    valor = resultado = num
    acumula = str(num)
    if show == True:
        while valor > 1:
            valor -= 1
            resultado *= valor
            acumula = acumula + ' x ' + str(valor)
        return acumula + ' = ' + str(resultado)
    else:
        while valor > 1:
            valor -= 1
            resultado *= valor
        return resultado





# Lógica
linha('-', 31, 40)
print(fatorial(5, True))
help(fatorial)