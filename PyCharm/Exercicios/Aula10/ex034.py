print('Vamos calcular o aumento do seu salário')
salario = float(input('Digite o valor do seu salário R$'))
if salario > 1250:
    aumento = salario * 0.10
    print('Seu \033[4;31maumento\033[m será de \033[1;34mR${:.2f}\033[m, salário total R${:.2f}'.format(aumento, salario + aumento))
else:
    aumento = salario * 0.15
    print('Seu \033[4;33maumento\033[m será de \033[1;36mR${:.2f}\033[m, salário toral R${:.2f}'.format(aumento, salario + aumento))
