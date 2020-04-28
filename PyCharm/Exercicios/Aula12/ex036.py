# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mCÁLCULO DE EMPRÉSTIMO BANCÁRIO PARA COMPRA DE IMÓVEL\033[m')

# Objetos
vcasa = float(input('\033[30mQual o valor do imóvel R$?:\033[m '))
salario = float(input('\033[30mQual o seu salário R$?:\033[m '))
anos = float(input('\033[30mEm quantos anos será pago o empréstimo?:\033[m '))
mensal = vcasa / (anos * 12)
limite = salario * (30 / 100)

# Lógica
if mensal < limite:
    print('Seu empréstimo foi \033[32maprovado\033[m, o valor da sua prestação será R${:.2f}'.format(mensal))
else:
    print('Seu empréstimo foi \033[31mnegado!\033[m O valor mensal de R${:.2f}, ultrapassa 30% (R${:.2f}) do seu salário'.format(mensal, limite))

