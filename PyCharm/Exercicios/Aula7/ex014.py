print('Vamos converter \033[31m°C\033[m em \033[31m°F\033[m')
c = float(input('Digite o valor em °C '))
print('O valor é {}°F'.format(((9 * c) / 5) + 32))
# Utilizado os parênteses no cálculo apenas para ficar mais fácil a leitura do código