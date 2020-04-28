nome = str(input('Digite o nome completo: ')).strip().split()
q = len(nome) - 1
print('Primeiro nome: \033[34m{}\033[m'.format(nome[0]))
print('Último nome: \033[32m{}\033[m'.format(nome[q]))
