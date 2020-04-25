num = str(input('Digite um número inteiro com até 4 digitos: '))
num = num.rjust(4, ' ')
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))

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