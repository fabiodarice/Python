# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mCÁLCULO DO IMC DE UMA PESSOA\033[m')

# Objetos
peso = float(input('\033[30mDigite o peso em kg:\033[m '))
altura = float(input('\033[30mDigite a altura em m:\033[m '))
imc = peso / altura**2
abaixo = 18.5
ideal = 25
sobrepeso = 30
obesidade = 40

# Lógica
if imc < abaixo:
    print('Seu IMC é \033[4;34m{:.2f}\033[m, você está \033[1;31mABAIXO\033[m do peso!'.format(imc))
elif imc >= abaixo and imc <= ideal:
    print('Seu IMC é \033[4;34m{:.2f}\033[m, você está com o peso \033[1;32mIDEAL!\033[m'.format(imc))
elif imc > ideal and imc <= sobrepeso:
    print('Seu IMC é \033[4;34m{:.2f}\033[m, você está com \033[1;31mSOBREPESO!\033[m'.format(imc))
elif imc > sobrepeso and imc <= obesidade:
    print('Seu IMC é \033[4;34m{:.2f}\033[m, você está com \033[1;31mOBESIDADE!\033[m'.format(imc))
elif imc > obesidade:
    print('Seu IMC é \033[4;34m{:.2f}\033[m, você está com \033[1;31mOBESIDADE MÓRBIDA!\033[m'.format(imc))
