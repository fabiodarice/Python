vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado pois sua velocidade foi de {}km/h e valor da sua multa é R${:.2f}'. format(vel, multa))
else:
    print('Sua velocidade está dentro do permitido!')