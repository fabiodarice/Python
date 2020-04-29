# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mCOMPARAÇÃO ENTRE DOIS NÚMEROS INTEIROS\033[m')

# Obejtos
n1 = int(input('\033[30mDigite o primeiro número inteiro:\033[m '))
n2 = int(input('\033[30mDigite o segundo número inteiro:\033[m '))

# Lógica
if n1 > n2:
    print('\033[1;33m-\033[m O \033[1;33mprimeiro valor\033[m é \033[1;34mmaior\033[m')
elif n1 < n2:
    print('\033[1;33m-\033[m O \033[1;33msegundo valor\033[m é \033[1;34mmaior\033[m')
else:
    print('\033[1;33m- Não existe\033[m valor maior, os dois são \033[1;34miguais\033[m')