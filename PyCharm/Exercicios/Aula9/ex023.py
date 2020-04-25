num = str(input('Digite um número inteiro com até 4 digitos: '))
q = len(num)
if q == 1:
    print('Unidade: {}'.format(num))
#    print('Dezena: {}'.format(''))
#    print('Centena: {}'.format(''))
#    print('Milhar: {}'.format(''))
if q == 2:
    print('Unidade: {}'.format(num[1]))
    print('Dezena: {}'.format(num[0]))
#    print('Centena: {}'.format(''))
#    print('Milhar: {}'.format(''))
if q == 3:
    print('Unidade: {}'.format(num[2]))
    print('Dezena: {}'.format(num[1]))
    print('Centena: {}'.format(num[0]))
#    print('Milhar: {}'.format(''))
if q == 4:
    print('Unidade: {}'.format(num[3]))
    print('Dezena: {}'.format(num[2]))
    print('Centena: {}'.format(num[1]))
    print('Milhar: {}'.format(num[0]))
if q > 4:
    print('Você digitou um número maior que 4 digitos!')