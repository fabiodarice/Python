# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mUM PRINT ESPECIAL\033[m')

# Objetos


# Funções
def escreva(texto):
    print('~' * (len(texto) + 4))
    print(f'{texto:^{(len(texto) + 4)}}')
    print('~' * (len(texto)+ 4))


# Lógica
escreva('Fábio')
escreva('Fábio Darice')
escreva('Fábio Darice da Silva')