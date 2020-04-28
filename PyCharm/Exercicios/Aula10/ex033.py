cores = {'vm':'\033[31m',
         'az':'\033[34m',
         'fim':'\033[m'}
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
menor = num1 #foi adotado nesta linha que o primeiro número digitado é o menor, caso não seja as próximas linhas
#irão corrigir
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
maior = num1 #foi adotado nesta linha que o primeiro número digitado é o maior, caso não seja as próximas linhas
#irão corrigir
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O menor número é {}{}{} e o maior número é {}{}{}'.format(cores['vm'], menor, cores['fim'], cores['az'], maior, cores['fim']))
