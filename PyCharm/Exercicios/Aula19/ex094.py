# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mUNINDO DICIONÁRIOS E LISTAS\033[m')

# Objetos
dados = []
somaidades = 0

# Lógica
while True:
    dados.append({'Nome':str(input('Nome: ')).strip().capitalize(),
                  'Sexo':str(input('Sexo: [M/F] ')).strip().upper(),
                  'Idade':int(input('Idade: '))})

    somaidades += dados[len(dados) - 1]['Idade']

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('\033[31m-=\033[m' * 30)

print(f'O grupo tem {len(dados)} pessoas.')
print(f'A média de idade é de {somaidades / len(dados):.1f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for c, info in enumerate(dados):
    for k, v in dados[c].items():
        if k == 'Sexo' and v == 'F':
            print(f'{dados[c]["Nome"]} ', end='')
print()

print(f'Lista das pessoas que estão acima da média:')
for c, info in enumerate(dados):
    for k, v in dados[c].items():
        if k == 'Idade' and v > somaidades / len(dados):
            print(f'nome = {dados[c]["Nome"]}; sexo = {dados[c]["Sexo"]}; idade = {dados[c]["Idade"]};')
            print()

print('<< ENCERRADO >>')