from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('O valor da hipotenusa é {:.2f}'.format(hypot(co, ca)))