from random import randint
from time import sleep
print('\033[34m-=-\033[m' * 30)
print('Tente adivinhar o número escolhido pelo computador que será entre 0 e 5')
print('\033[34m-=-\033[m' * 30)
num_u = int(input('Digite um número entre 0 e 5 que você acha que o computado escolheu: '))
print('\033[33mPROCESSANDO ...\033[m')
sleep(2)
num_c = randint(0, 5)
if num_u == num_c:
    print('Parabéns, você \033[34macertou\033[m!')
else:
    print('Infelizmente você \033[31merrou\033[m, o computador escolheu {}, tente novamente!'.format(num_c))