# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mSEQUÊNCIA DE FIBONACCI\033[m')

# Objetos
a = 0
b = 1
x = 0
incremento = 0

# Lógica
termos = int(input('\033[30mDeseja mostrar quantos termos?:\033[m '))

print(a, b, end=' ')

while (incremento + 2) != termos:
    incremento = incremento + 1
    x = a + b
    print(x, end=' ')

    if incremento % 2 != 0:
        a = x
    if incremento % 2 == 0:
        b = x