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
    for c in range(0, 11):
        print(f'{num} x {c:2} = {num * c}')
print('\033[33mPROGRAMA TABUADA ENCERRADO\033[m, \033[1;34mVolte sempre!\033[m')