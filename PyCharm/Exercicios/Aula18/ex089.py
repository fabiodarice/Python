# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mBOLETIM COM LISTAS COMPOSTAS\033[m')

# Objetos
dados = list()

# Lógica
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('-=' * 30)

print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>10}')
print('-' * 30)
for n, info in enumerate(dados):
    print(f'{n:<5}{info[0]:<10}{info[2]:>10.1f}')

print('-=' * 30)

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if mostrar == 999:
        break

    while mostrar >= len(dados):
        print('Valor inválido. ', end='')
        mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    print(f'Notas de {dados[mostrar][0]} são {dados[mostrar][1]}')