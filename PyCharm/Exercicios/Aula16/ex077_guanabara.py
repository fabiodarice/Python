# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mCONTANDO VOGAIS EM TUPLA\033[m')

# Objetos
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
          'praticar', 'trabalhar', 'mercador', 'programador', 'futuro')

# Lógica
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')