# Importação de bibliotecas
from time import sleep

# Título do programa
print('\033[1;34;40mFUNÇÃO QUE DESCOBRE O MAIOR\033[m')

# Objetos


# Funções
def maior(*num):
    m = qtd = 0
    print('Analisando os valores passados...')
    for n in num:
        print(n, '', end='')
        qtd += 1
        if n > m:
            m = n
        sleep(0.5)
    print(f'Foram informados {qtd} valores ao todo.')
    print(f'O maior valor informado foi {m}')
    print('-=' * 30)

# Lógica
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()