nome = input('\033[7mOlá, qual é seu nome? \033[m')
n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
print('\033[34m{}\033[m, suas notas foram as seguintes, {} e {}, e sua média foi {}'.format(nome, n1, n2, (n1+n2)/2))
