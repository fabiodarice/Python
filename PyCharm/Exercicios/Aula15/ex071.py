# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mSIMULADOR DE CAIXA ELETRÔNICO\033[m')

# Objetos
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0

# Lógica
print('\033[34m=\033[m' * 50)
print(f'\033[1;33m{"BANCO CEV":^50}\033[m')
print('\033[34m=\033[m' * 50)
valor = int(input('\033[30mQue valor você que sacar R$:\033[m '))

while True:
    if valor >= 50:
        nota50 = valor // 50
        resto = valor % 50
        if resto == 0:
            break
        else:
            valor = valor - (nota50 * 50)

    if valor >= 20:
        nota20 = valor // 20
        resto = valor % 20
        if resto == 0:
            break
        else:
            valor = valor - (nota20 * 20)

    if valor >= 10:
        nota10 = valor // 10
        resto = valor % 10
        if resto == 0:
            break
        else:
            valor = valor - (nota10 * 10)

    if valor >= 1:
        nota1 = valor // 1
        break

print(f'Total de \033[1;31m{nota50}\033[m cédulas de R$50')
print(f'Total de \033[1;32m{nota20}\033[m cédulas de R$20')
print(f'Total de \033[1;33m{nota10}\033[m cédulas de R$10')
print(f'Total de \033[1;34m{nota1}\033[m cédulas de R$10')
print('\033[34m=\033[m' * 50)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')