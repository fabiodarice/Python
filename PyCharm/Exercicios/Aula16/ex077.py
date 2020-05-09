# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mCONTANDO VOGAIS EM TUPLA\033[m')

# Objetos
varias = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
          'praticar', 'trabalhar', 'mercador', 'programador', 'futuro')
tamvarias = len(varias)
vogais = ('a', 'e', 'i', 'o', 'u')
x = 0
y = 0
z = 0

# Lógica
while z < tamvarias:
    palavra = varias[z]
    tamanho = len(palavra)
    print(f'\nNa palavra {palavra.upper()} tem as vogais', '', end='')
    while y < tamanho:
        letra = palavra[y]
        while True:
            if letra == vogais[x]:
                print(vogais[x], '', end='')
                x = 0
                y = y + 1
                break
            else:
                x = x + 1
            if x == 5:
                x = 0
                y = y + 1
                break
    x = 0
    y = 0
    z = z + 1