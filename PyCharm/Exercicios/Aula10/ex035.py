from math import trunc
print('Vamos verificar a condição de existência de um triângulo')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunfa reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('reta 1', '\033[31m-\033[m' * trunc(r1), 'reta 2', '\033[33m-\033[m' * trunc(r2), 'reta 3', '\033[34m-\033[m' * trunc(r3))
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo')
    print('reta 1', '\033[31m-\033[m' * trunc(r1), 'reta 2', '\033[33m-\033[m' * trunc(r2), 'reta 3', '\033[34m-\033[m' * trunc(r3))