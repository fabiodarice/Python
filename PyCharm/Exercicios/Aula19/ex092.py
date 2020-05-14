# Importação de bibliotecas
from datetime import date

# Título do programa
print('\033[1;34;40mCADASTRO DE TRABALHADOR EM PYTHON\033[m')

# Objetos
dados = {'Nome':str(input('Nome: ')).strip().capitalize(),
         'idade':date.today().year - int(input('Ano de Nascimento: ')),
         'ctps':int(input('Carteira de Trabalho (0 não tem): '))}


# Lógica
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = (35 - (date.today().year - dados['contratação'])) + dados['idade']

print('\033[33m-=\033[m' * 30)

for k, v in dados.items():
    print(f'{k} tem o valor {v}')