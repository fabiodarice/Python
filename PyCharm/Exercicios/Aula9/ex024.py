nome = str(input('\033[33;44mDigite o nome de uma cidade:\033[m ')).strip().capitalize().split()
print('O nome da cidade começa com a palavras "Santo"?: {}'.format(nome[0] == 'Santo'))

# Forma como o Gustavo Guanabara resolveu, mas tem uma falha, se digitar "santos" ele considera True, pois
# o programa só está lendo os 5 primeiros caracteres
#name = str(input('Digite o nome da cidade que você nasceu: ')).strip()
#print('O nome da cidade começa com a palavra "Santo"?', name[:5].lower() == 'santo')