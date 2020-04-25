nome = str(input('Digite o nome completo: ')).strip().split()
q = len(nome) - 1
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[q]))
