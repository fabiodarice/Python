from random import choice
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
alunos = [a1, a2, a3, a4]
print('O aluno escolhido para apagar o quadro foi o \033[31m{}\033[m'.format(choice(alunos)))

