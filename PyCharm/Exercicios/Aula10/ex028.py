from random import randint
from time import sleep
print('-=-' * 30)
print('Tente adivinhar o número escolhido pelo computador que será entre 0 e 5')
print('-=-' * 30)
num_u = int(input('Digite um número entre 0 e 5 que você acha que o computado escolheu: '))
print('PROCESSANDO ...')
sleep(2)
num_c = randint(0, 5)
if num_u == num_c:
    print('Parabéns, você acertou!')
else:
    print('Infelizmente você errou, o computador escolheu {}, tente novamente!'.format(num_c))