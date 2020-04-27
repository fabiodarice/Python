num = int(input('Digite um número para verificar se é par ou impar: '))
verif = num % 2
if verif == 0:
    print('O número digitado é par')
else:
    print('O número digitado é ímpar')