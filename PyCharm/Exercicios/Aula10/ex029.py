vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi \033[31mmultado\033[m pois sua \033[34mvelocidade\033[m foi de \033[4;31m{}km/h\033[m e valor da sua multa é R${:.2f}'. format(vel, multa))
else:
    print('Sua velocidade está dentro do permitido!')