# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mSIMULADOR DE CAIXA ELETRÔNICO\033[m')

# Objetos
céd = 50
totcéd = 0

# Lógica
print('\033[34m=\033[m' * 50)
print(f'\033[1;33m{"BANCO CEV":^50}\033[m')
print('\033[34m=\033[m' * 50)
valor = int(input('\033[30mQue valor você que sacar R$:\033[m '))
total = valor

'''Esta lógica foi desenvolvida pelo prof. Gustavo Guanabara, mas tinha um problema
caso retirasse uma valor menor que R$50, isso foi corrigido acrescentando as linhas de 
22 a 27'''

if total >= 20 and total < 50:
    céd = 20
elif total >= 10 and total < 20:
    céd = 10
elif total >= 1 and total < 10:
    céd = 1

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
            if céd == 50:
                céd = 20
            elif céd == 20:
                céd = 10
            elif céd == 10:
                céd = 1
            totcéd = 0
            if total == 0:
                break

print('\033[34m=\033[m' * 50)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')