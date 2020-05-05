# Importação de bibiotecas


# Título do programa
print('\033[1;34;40mMENU DE OPÇÕES\033[m')

# Objetos
menu = 0
n1 = 0
n2 = 0
maior = 0

# Lógica
while menu != 5:
    n1 = int(input('\033[30mDigite o primeiro número:\033[m '))
    n2 = int(input('\033[30mDigite o segundo número:\033[m '))
    print('\033[34m-=-\033[m' * 20)
    print('\033[30mO que você deseja fazer?\033[m'
          '\n\033[33m[1]\033[m \033[34msomar\033[m'
          '\n\033[33m[2]\033[m \033[34mmultiplicar\033[m'
          '\n\033[33m[3]\033[m \033[34mmaior\033[m'
          '\n\033[33m[4]\033[m \033[34mnovos números\033[m'
          '\n\033[33m[5]\033[m \033[34msair do programa\033[m')
    menu = int(input('\033[30mEscolha uma das opções acima:\033[m '))
    print('\033[34m-=-\033[m' * 20)
    if menu == 1:
        print('O valor da soma dos valores é \033[4;34m{}\033[m'.format(n1 + n2))
    if menu == 2:
        print('O valor da multiplicação dos valores é \033[4;34m{}\033[m'.format(n1 * n2))
    if menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor digitado foi \033[4;34m{}\033[m'.format(maior))
    if menu < 1 or menu > 5:
        print('Opção inválida, tente novamente!')
print('\033[33mVOCÊ SAIU DO PROGRAMA!\033[m')