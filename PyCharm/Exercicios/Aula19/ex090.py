# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mDICIONÁRIO EM PYTHON\033[m')

# Objetos
dados = {}

# Lógica
dados = {'Nome':str(input('Nome: ')).strip().capitalize()}
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))

if dados['Média'] >= 7:
    dados['Situação'] = 'APROVADO'
else:
    dados['Situação'] = 'REPROVADO'

for k, v in dados.items():
    print(f'{k} é igual a {v}')