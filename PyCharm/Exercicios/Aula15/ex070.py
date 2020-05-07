# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mESTATÍTSTICAS EM PRODUTOS\033[m')

# Objetos
gasto = 0
caros = 0
barato = 0
produtomaisbarato = ''

# Lógica
print('\033[34m-\033[m' * 50)
print(f'\033[1;33m{"LOJA SUPER BARATÃO":^50}\033[m')
print('\033[34m-\033[m' * 50)

while True:
    produto = str(input('\033[30mNome do produto:\033[m ').strip().title())
    valor = float(input('\033[30mPreço R$:\033[m '))

    gasto += valor

    if valor > 1000:
        caros += 1

    if barato == 0 or valor < barato:
        barato = valor
        produtomaisbarato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\033[30mQuer continuar: [S/N]\033[m ')).strip().upper()
    if continuar == 'N':
        break

print(f'\033[1;33m{" FIM DO PROGRAMA ":=^50}\033[m')
print(f'O total da compra foi \033[4;34mR${gasto:.2f}\033[m')
print(f'Temos \033[1;32m{caros}\033[m produtos custando mais de R$1000,00')
print(f'O produto mais barato foi \033[1;31m{produtomaisbarato}\033[m que custa \033[4;34mR${barato:.2f}\033[m')