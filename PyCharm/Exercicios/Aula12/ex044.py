# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mCÁLCULO DO VALOR DE UM PRODUTO CONFORME OPÇÃO DE PAGAMENTO\033[m')

# Objetos
preco = float(input('\033[30mDigite o valor do produto R$:\033[m '))
pagamento = str(input('Qual será a forma de pagamento? Dinheiro, cheque ou cartão?: ')).strip().lower()
desconto1 = 10
desconto2 = 5
juros = 20

# Lógica
if pagamento == 'dinheiro' or pagamento == 'cheque':
    print('Você tem \033[1;33m{}%\033[m de desconto, o valor do produto com o desconto é de \033[1;34mR${:.2f}\033[m'.format(desconto1, preco - (preco * (desconto1 / 100))))
elif pagamento == 'cartão':
    parcelas = int(input('\033[30mSerá pago em quantas parcelas?:\033[m '))
    if parcelas == 1:
        print('Você tem \033[1;33m{}%\033[m de desconto, o valor do produto com o desconto é de \033[1;34mR${:.2f}\033[m'.format(desconto2, preco - (preco * (desconto2 / 100))))
    if parcelas == 2:
        print('O valor do seu produto é de \033[mR${:.2f}\033[m'.format(preco))
    if parcelas > 2:
        print('Você terá um acrécimo de \033[1;31m{}%\033[m de juros, o valor do produto com os juros é de \033[1;34mR${:.2f}\033[m'.format(juros, preco + (preco * (juros / 100))))
