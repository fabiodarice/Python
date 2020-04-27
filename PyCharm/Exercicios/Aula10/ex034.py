print('Vamos calcular o aumento do seu salário')
salario = float(input('Digite o valor do seu salário R$'))
if salario > 1250:
    aumento = salario * 0.10
    print('Seu aumento será de R${:.2f}, salário total R${:.2f}'.format(aumento, salario + aumento))
else:
    aumento = salario * 0.15
    print('Seu aumento será de R${:.2f}, salário toral R${:.2f}'.format(aumento, salario + aumento))
