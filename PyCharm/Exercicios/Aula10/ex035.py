print('Vamos verificar a condição de existência de um triângulo')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunfa reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo')