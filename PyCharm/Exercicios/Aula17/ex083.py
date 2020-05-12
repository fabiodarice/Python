# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mVALIDANDO EXPRESSÕES MATEMÁTICAS\033[m')

# Objetos
lista = list()

# Lógica
expressão = (str(input('\033[30mDigite a expressão:\033[m ')).strip().lower())
for simbolo in expressão:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')