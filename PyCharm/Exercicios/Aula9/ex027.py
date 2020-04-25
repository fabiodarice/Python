nome = str(input('Digite o nome completo: '))
s = nome.split()
q = len(s)
q = q - 1
print('Primeiro nome: {}'.format(s[0]))
print('Último nome: {}'.format(s[q]))
