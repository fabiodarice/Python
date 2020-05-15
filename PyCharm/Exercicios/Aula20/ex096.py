# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mFUNÇÃO QUE CALCULA ÁREA\033[m')

# Objetos


# Funções
def área(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m²')


# Lógica
print('Controle de Terrenos')
print('-' * 40)

lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
área(lar, comp)
