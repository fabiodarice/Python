dist = int(input('Digite quantos km terá a sua viagem: '))
if dist <= 200:
    print('O valor da sua passagem será \033[34mR${:.2f}\033[m'.format(dist * 0.5))
else:
    print('O valor da sua passagem será \033[34mR${}\033[m'.format(dist * 0.45))
