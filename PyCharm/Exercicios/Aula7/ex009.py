print('Vamos aprender tabuada')
cores = {'fim': '\033[m',
         'vm': '\033[31m',
         'az': '\033[34m'}
n = int(input('Digite um valor inteiro '))
print(cores['vm'] + '-' * 12, cores['fim'])
print(cores['az'] + '{} x {:2} = {}'.format(n, 0, n*0))
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10), cores['fim'])
print(cores['vm'] + '-' * 12, cores['fim'])