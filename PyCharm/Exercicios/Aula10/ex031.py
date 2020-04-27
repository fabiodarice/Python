dist = int(input('Digite quantos km terá a sua viagem: '))
if dist <= 200:
    print('O valor da sua passagem será R${:.2f}'.format(dist * 0.5))
else:
    print('O valor da sua passagem será R${}'.format(dist * 0.45))
