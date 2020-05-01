# Importação de bibliotecas


# Título do programa
print('\033[1;34;40m\033[m')

# Objetos
a = 0
b = 0
d = 0
velho = ''

# Lógica
for c in range(0, 4):
    nome = str(input('\033[30mDigite o nome:\033[m ')).strip().title()
    idade = int(input('\033[30mDigite a idade:\033[m '))
    sexo = str(input('\033[30mDigite o sexo:\033[m ')).strip().lower()
    a = a + idade
    if sexo == 'masculino' and idade > b:
        b = idade
        velho = nome
    if sexo == 'feminino' and idade < 20:
        d = d + 1
print('A média da idade do grupo é \033[4;34m{}\033[m'.format(a / 4))
print('O nome do homem mais velho é \033[33m{}\033[m'.format(velho))
print('A quantidade de mulheres com menos de 20 anos é \033[1;31m{}\033[m'.format(d))