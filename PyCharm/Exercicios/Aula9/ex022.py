# Foi colocado a função strip() no final da primeira linha para já garantir a eliminação dos espaços no começo
# e final do nome caso alguém digite na hora de inserir o nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Todas as letras maiúsculas {}'.format(nome.upper()))
print('Todas as letras minúsculas {}'.format(nome.lower()))
print('Quantidade de letras sem espaço {}'.format(len(''.join(nome.split()))))
# Outra forma de contar a quantidade de letras sem contar os espaços
#print('Quantidade de letras sem espaço {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de letras no primeiro nome {}'.format(len(nome.split()[0])))
# Outra forma de contar a quantidade de letras do primeiro nome
#print('Quantidade de letas no primeiro nome {}'.format(nome.find(' ')))
