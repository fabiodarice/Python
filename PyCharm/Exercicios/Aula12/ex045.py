# Importação de bibliotecas
from random import choice
from emoji import emojize

# Título do programa
print('\033[1;34;40mJOKENPÔ\033[m')

# Objetos
jogador = str(input('\033[30mEscolha entre pedra, papel ou tesoura:\033[m ')).strip().lower()
computador = ['pedra', 'papel', 'tesoura']
pedra = emojize(':fist:', use_aliases=True)
papel = emojize(':hand:', use_aliases=True)
tesoura = emojize(':v:', use_aliases=True)
computador = choice(computador)

# Lógica
if jogador == 'pedra' and computador == 'tesoura':
    print('Você: {} x {} Computador'.format(pedra, tesoura))
    print('\033[1;32mParabéns!\033[m Você \033[4;34mVENCEU!\033[m')
elif jogador == 'pedra' and computador == 'pedra':
    print('Você escolheu {} e computador escolheu {}'.format(pedra, pedra))
    print('Deu \033[4;34mEMPATE!\033[m')
elif jogador == 'pedra' and computador == 'papel':
    print('Você escolheu {} e o computador escolheu {}'.format(pedra, papel))
    print('Você \033[4;31mPERDEU!\033[m')

elif jogador == 'papel' and computador == 'pedra':
    print('Você escolheu {} e o computador escolheu {}'.format(papel, pedra))
    print('\033[1;32mParabéns!\033[m Você \033[4;34mVENCEU!\033[m')
elif jogador == 'papel' and computador == 'papel':
    print('Você escolheu {} e o computador escolheu {}'.format(papel, papel))
    print('Deu \033[4;34mEMPATE!\033[m')
elif jogador == 'papel' and computador == 'tesoura':
    print('Você escolheu {} e o computador escolheu {}'.format(papel, tesoura))
    print('Você \033[4;31mPERDEU!\033[m')

elif jogador == 'tesoura' and computador == 'papel':
    print('Você escolheu {} e o computador escolheu {}'.format(tesoura, papel))
    print('\033[1;32mParabéns!\033[m Você \033[4;34mVENCEU!\033[m')
elif jogador == 'tesoura' and computador == 'tesoura':
    print('Você escolheu {} e o computador escolheu {}'.format(tesoura, tesoura))
    print('Deu \033[4;34mEMPATE!\033[m')
elif jogador == 'tesoura' and computador == 'pedra':
    print('Você escolheu {} e o computador escolheu {}'.format(tesoura, pedra))
    print('Você \033[4;31mPERDEU!\033[m')