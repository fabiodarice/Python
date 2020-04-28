frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print('A letra \033[4;31m"A"\033[m aparece {} vezes na frase'.format(frase.count('A')))
print('A Primeira vez em que aparece a letra \033[4;31m"A"\033[m é na posição {}'.format(frase.find('A')))
print('A Última vez em que aparece a letra \033[4;31m"A"\033[m é na posição {}'.format(frase.rfind('A')))


