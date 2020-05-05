# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mVERIFICAÇÃO\033[m')

# Objetos
sexo = ''

# Lógica
sexo = str(input('\033[30mInforme seu sexo [M/F]:\033[m ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\033[mDados inválidos, por favor, informe seu sexo [M/F]:\033[m ')).strip().upper()[0]
print('\033[4;34mSexo {} registrado com sucesso\033[m'.format(sexo))
