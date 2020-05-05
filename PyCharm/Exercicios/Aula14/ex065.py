# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mMAIOR E MENOR VALORES\033[m')

# Objetos
num = 0
digitados = 0
soma = 0
continuar = ''
maior = 0
menor = 0

# Lógica
while continuar in 's':
    num = int(input('\033[30mDigite um valor:\033[m '))
    digitados += 1
    soma += num
    if num > maior:
        maior = num
    if menor == 0 or num < menor:
        menor = num
    continuar = str(input('\033[30mDeseja continuar digitando valores [\033[33ms\033[mim ou \033[31mn\033[mão]?:\033[m ')).strip().lower()
    while continuar not in 'sn':
        print('\033[1;31mOpção inválida tente novamente!\033[m')
        continuar = str(input('\033[30mDeseja continuar digitando valores [\033[33ms\033[mim ou \033[31mn\033[mão]?:\033[m ')).lower()
print('A média entre os {:.1f} números digitados foi {}, o menor número foi {} e o maior foi {}'.format(digitados, soma / digitados, menor, maior))