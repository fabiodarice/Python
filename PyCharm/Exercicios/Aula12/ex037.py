# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mCONVERSOR DE BASE NÚMERICA\033[m')

# Objetos
num = int(input('\033[30mDigite um número inteiro qualquer:\033[m '))
print('''\033[30mPara qual base deve ser convertido?
[1] binário
[2] octal
[3] hexadecimal\033[m ''')
base = int(input('\033[30mEscolha uma opção:\033[m '))

# Lógica
if base == 1:
    print('O número {} convertido para binário é {}{}{}'.format(num, '\033[1;32m', bin(num)[2:], '\033[m'))
elif base == 2:
    print('O número {} convertido para octal é {}{}{}'.format(num, '\033[1;33m', oct(num)[2:], '\033[m'))
elif base == 3:
    print('O número {} convertido para hexadecimal é {}{}{}'.format(num, '\033[1;34m', hex(num)[2:], '\033[m'))
else:
    print('\033[1;31mVocê não escolheu uma base válida!\033[m')
