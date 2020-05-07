# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mTABUADA V3.0\033[m')

# Objetos
num = 0

# Lógica
while True:
    print('-' * 30)
    num = int(input('\033[30mQuer ver a tabuada de qual valor?:\033[m '))
    print('-' * 30)
    if num < 0:
        break
    print(f'{num} x {0:2} = {num * 0}\n'
          f'{num} x {1:2} = {num * 1}\n'
          f'{num} x {2:2} = {num * 2}\n'
          f'{num} x {3:2} = {num * 3}\n'
          f'{num} x {4:2} = {num * 4}\n'
          f'{num} x {5:2} = {num * 5}\n'
          f'{num} x {6:2} = {num * 6}\n'
          f'{num} x {7:2} = {num * 7}\n'
          f'{num} x {8:2} = {num * 8}\n'
          f'{num} x {9:2} = {num * 9}\n'
          f'{num} x {10:2} = {num * 10}')
print('\033[33mPROGRAMA TABUADA ENCERRADO\033[m, \033[1;34mVolte sempre!\033[m')