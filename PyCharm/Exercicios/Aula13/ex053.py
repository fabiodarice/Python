# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mVERIFICA SE A FRASE É PALÍNDROMO\033[m')

# Objetos
frase = str(input('\033[30mDigite uma frase:\033[m ')).strip().lower().split()
res = ''.join(frase)
tamanho = len(res)
contrario = ''

# Lógica
for c in range(tamanho, 0, -1):
    contrario = contrario + res[c - 1]
if res == contrario:
    print('Essa frase é \033[4;34mPALÍNDROMO!!!\033[m')
else:
    print('Essa frase \033[31mNÃO\033[m é PALÍNDROMO!!!')