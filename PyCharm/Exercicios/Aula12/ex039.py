# Importação de bibliotecas
from datetime import date

# Título do programa
print('\033[1;34;40mVERIFICAR ALISTAMENTO MILITAR\033[m')

# Objetos
ano = int(input('\033[30mDigite o ano do seu nascimento:\033[m '))
idade = date.today().year - ano
alistamento = 18
falta = alistamento - idade
passou = idade - alistamento

# Lógica
if idade < alistamento:
    print('Você ainda irá se alistar ao serviço militar, falt{} {} an{}'.format('am' if falta > 1 else 'a', falta, 'os' if falta > 1 else 'o'))
elif idade == alistamento:
    print('Está na hora de você se alistar ao serviço militar')
elif idade > alistamento:
    print('O tempo de você se alistar ao serviço militar já passou em {} an{}'.format(passou, 'os' if passou > 1 else 'o'))
