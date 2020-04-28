dias = int(input('Quantidade de \033[33mdias\033[m com o carro alugado '))
km = int(input('Quantidade de km rodados '))
print('O valor a ser pago é R${:.2f}'.format((dias*60)+(km*0.15)))