# Foi colocado a função strip() no final da primeira linha para já garantir a eliminação dos espaços no começo
# e final do nome caso alguém digite na hora de inserir o nome
nome = str(input('Digite seu nome completo: ')).strip()
print('\033[31mTodas as letras maiúsculas\033[m {}'.format(nome.upper()))
print('\033[32mTodas as letras minúsculas\033[m {}'.format(nome.lower()))
print('\033[33mQuantidade de letras sem espaço\033[m {}'.format(len(''.join(nome.split()))))
# Outra forma de contar a quantidade de letras sem contar os espaços
#print('Quantidade de letras sem espaço {}'.format(len(nome) - nome.count(' ')))
print('\033[34mQuantidade de letras no primeiro nome {}\033[m'.format(len(nome.split()[0])))
# Outra forma de contar a quantidade de letras do primeiro nome
#print('Quantidade de letas no primeiro nome {}'.format(nome.find(' ')))
