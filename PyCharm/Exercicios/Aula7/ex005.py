n = int(input('Digite um número '))
print('O número digitado foi \033[1;31m{}\033[m, seu antecessor é \033[1;30m{}\033[m e seu sucessor é \033[32m{}\033[m'. format(n, n-1, n+1))

