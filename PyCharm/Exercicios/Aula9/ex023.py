num = str(input('Digite um número inteiro com até 4 digitos: '))
num = num.rjust(4, ' ')
print('\033[1;34;41mUnidade:\033[m {}'.format(num[3]))
print('\033[1;34;42mDezena:\033[m {}'.format(num[2]))
print('\033[1;34;43mCentena:\033[m {}'.format(num[1]))
print('\033[1;33;44mMilhar:\033[m {}'.format(num[0]))

# Fazendo pelo método matemático

#num = int(input('Digite um número inteiro com até 4 digitos: '))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('Unidade {}'.format(u))
#print('Dezena {}'.format(d))
#print('Centena {}'.format(c))
#print('Milhar {}'.format(m))