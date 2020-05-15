# Importação de bibliotecas
from time import sleep

# Título do programa
print('\033[1;34;40mFUNÇÃO DE CONTADOR\033[m')

# Objetos


# Funções
def contador(inicio, fim, passo):
    if inicio > fim:
        fim -= passo
        passo *= -1
    else:
        fim += 1

    for c in range(inicio, fim, passo):
        print(f'{c}', '', end='')
        c += 1
        sleep(0.2)
    print('FIM!')


# Lógica
print('-=' * 30)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)

print('-=' * 30)
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)

print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

if i > f and p < 0:
    p *= -1
elif p == 0:
    p = 1

print('-=' * 30)
print(f'Contagem de {i} até {f} de {p} em {p}')
contador(i, f, p)
