print('\033[36;40mVamos calcular a quantidade necessária de tinta para pintar uma parede\033[m')
l = float(input('Digite a largura da parede em metros '))
a = float(input('Digite a altura da parede em metros '))
area = l*a
print('A área total da parede é {}m2, a quantidade total de tinta para pintar é {}l'.format(area, area/2))
