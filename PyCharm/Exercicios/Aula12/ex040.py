# Importação de bibliotecas


# Título do programa
print('\033[1;34;40mCÁLCULO DE NOTA MÉDIA PARA PASSAR DE ANO\033[m')

# Objetos
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
corte1 = 5
corte2 = 7

# Lógica
if media < corte1:
    print('Sua média foi de \033[1;33m{:.1f}\033[m, você foi \033[1;34mREPROVADO!\033[m'.format(media))
elif corte2 > media >= corte1:
    print('Sua média foi de \033[1;33m{:.1f}\033[m, você ficou de \033[1;34mRECUPERAÇÃO!\033[m'.format(media))
elif media >= corte2:
    print('Sua média foi de \033[1;33m{:.1f}\033[m, você foi \033[1;34mAPROVADO!\033[m'.format(media))