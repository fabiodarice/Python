# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mLISTA COM PARES E ÍMPARES\033[m')

# Objetos
valores = [[], []]

# Lógica
for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))

    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

valores[0].sort()
valores[1].sort()

print('=-' * 30)

print(f'Os valore pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
