# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mVÁRIOS NÚMEROS COM FLAG\033[m')

# Objetos
num = n = s = 0

# Lógica
while True:
    num = int(input('\033[30mDigite um número (999 para parar):\033[m '))
    if num == 999:
        break
    n += 1
    s += num
print(f'Você digitou \033[33m{n}\033[m números e a soma entre eles é \033[4;34m{s}\033[m')