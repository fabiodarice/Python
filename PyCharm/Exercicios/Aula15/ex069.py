# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mANÁLISE DE DADOS DO GRUPO\033[m')

# Objetos
maiores = 0
homens = 0
mulheres = 0
sexo = ''
continuar = ''

# Lógica
while continuar != 'N':
    print('\033[34m-\033[m' * 50)
    print(f'\033[1;33m{"CADASTRE UMA PESSOA":^50}\033[m')
    print('\033[34m-\033[m' * 50)

    idade = int(input('\033[30mIdade:\033[m '))
    sexo = str(input('\033[30mSexo: [M/F]\033[m ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('\033[30mSexo: [M/F]\033[m ')).strip().upper()

    if idade > 18:
        maiores += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres += 1

    continuar = str(input('\033[30mQuer continuar: [S/N]\033[m ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('\033[30mQuer continuar: [S/N]\033[m ')).strip().upper()
print(f'\033[1;33m{" FIM DO PROGRAMA ":=^50}\033[m')
print(f'Total de pessoas com mais de 18 anos: \033[4;34m{maiores}\033[m')
print(f'Ao todo temos \033[1;32m{homens} homens\033[m cadastrados')
print(f'E temos \033[1;31m{mulheres} mulheres\033[m com menos de 20 anos')