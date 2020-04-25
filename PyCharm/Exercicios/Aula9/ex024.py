nome = str(input('Digite o nome de uma cidade: '))
v = nome.split()
print('O nome da cidade começa com a palavras "Santo"?: {}'.format('Santo' in v[0]))
