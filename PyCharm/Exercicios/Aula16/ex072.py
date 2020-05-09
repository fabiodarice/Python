# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mNÚMERO POR EXTENSO\033[m')

# Objetos
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
     'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
     'dezenove', 'vinte')

# Lógica
while True:
    num = int(input('\033[30mDigite um número entre 0 e 20:\033[m '))
    if 0 <= num <= 20:
        break
    print('\033[30mTente novamente.\033[m ', end="")

print(f'Você digitou o número \033[4;34m{n[num]}\033[m')