n = float(input('Digite um número '))
print('\033[31m-=-' * 35, '\033[m')
print('\033[34mO número digitado foi {}, o dobro deste número é {}, o triplo é {} e sua raiz quadrada é {:.2f}\033[m'.format(n, n*2, n*3, n**(1/2)))
print('\033[31m-=-' * 35, '\033[m')
