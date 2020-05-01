# Importação de bibliotecas
from datetime import date

# Título do programa
print('\033[1;34;40mVERIFICA A MAIORIDADE\033[m')

# Objetos
ano = date.today().year
menores = 0
maiores = 0

# Lógica
for c in range(0, 7):
    nascimento = int(input('\033[30mDigite o ano de nascimento:\033[m '))
    if (ano - nascimento) >= 21:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('\033[4;34m{}\033[m ainda não antigiram a maioridade e \033[4;34m{}\033[m já são maiores'.format(menores, maiores))