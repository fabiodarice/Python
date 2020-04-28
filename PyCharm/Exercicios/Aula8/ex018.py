from math import radians, sin, cos, tan
n = float(input('Digite um valor de ângulo qualquer: '))
print('\033[31m' + '-=' * 20, '\033[m')
print('O valor do seno é {:.2f}'.format(sin(radians(n))))
print('O valor do cosseno é {:.2f}'.format(cos(radians(n))))
print('O valor da tangente é {:.2f}'.format(tan(radians(n))))
print('\033[31m' + '-=' * 20, '\033[m')
