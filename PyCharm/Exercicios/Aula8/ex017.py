from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('O valor da hipotenusa é \033[1;30;42m{:.2f}\033[m'.format(hypot(co, ca)))