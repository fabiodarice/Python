# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mLISTA ORDENADA SEM REPETIÇÕES\033[m')

# Objetos
valores = list()
pos = 0

# Lógica
for c in range(0, 5):
    n = int(input('\033[30mDigite um valor:\033[m '))
    while True:
        if len(valores) == 0:
            valores.append(n)
            print(f'Adicionado ao final da lista...')
            break
        elif n > valores[pos]:
            if pos == len(valores) - 1:
                valores.append(n)
                print(f'Adicionado ao final da lista...')
                pos = 0
                break
            else:
                pos = pos + 1
        else:
            valores.insert(pos, n)
            print(f'Adicionado na posição {pos} da lista...')
            pos = 0
            break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')