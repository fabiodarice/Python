print('Vamos somar dois números!')
n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o segundo número '))
r = n1 + n2
print('O resultado da soma entre {}{}{} e {}{}{} vale {}{}{}'.format('\033[32m', n1,'\033[m', '\033[36m', n2, '\033[m', '\033[4;31m', r, '\033[m'))
