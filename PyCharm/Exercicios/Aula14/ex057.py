# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mVERIFICAÇÃO\033[m')

# Objetos
sexo = ''

# Lógica
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite um sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != "F":
        print('Opção incorreta, favor digitar novamente!')
print('\033[4;34mFim!\033[m')
