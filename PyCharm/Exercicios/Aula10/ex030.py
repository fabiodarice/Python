num = int(input('Digite um número para verificar se é par ou impar: '))
verif = num % 2
if verif == 0:
    print('\033[1;34;43mO número digitado é par\033[m')
else:
    print('\033[1;34;45mO número digitado é ímpar\033[m')