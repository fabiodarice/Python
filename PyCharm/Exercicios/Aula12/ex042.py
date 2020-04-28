# Importação de bibliotecas
from math import trunc

# Título do programa
print('\033[1;34;40mVERIFICA A EXISTÊNCIA E O TIPO DO TRIÂNGULO\033[m')

# Objetos
s1 = float(input('\033[30mDigite o valor do primeiro segmento:\033[m '))
s2 = float(input('\033[30mDigite o valor do segundo segmento:\033[m '))
s3 = float(input('\033[30mDigite o valor do terceiro segmento:\033[m '))

# Lógica
print('\33[31m-=-\033[m' * 20)

print('segmento 1:', '\033[33m-\033[m' * trunc(s1))
print('segmento 2:', '\033[34m-\033[m' * trunc(s2))
print('segmento 3:', '\033[35m-\033[m' * trunc(s3))

print('\033[31m-=-\033[m' * 20)

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    if s1 == s2 and s1 == s3:
        print('Esses segmentos \033[1;32mformam\033[m um triângulo \033[1;34mEQUILÁTERO!\033[m')
    if s1 == s2 and s1 != s3 or s1 == s3 and s1 != s2:
        print('Esses segmentos \033[1;32mformam\033[m um triângulo \033[1;34mISÓSCELES!\033[m')
    if s1 != s2 and s1 != s3:
        print('Esses segmentos \033[1;32mformam\033[m um triângulo \033[1;34mESCALENO!\033[m')
else:
    print('Esses segmentos \033[1;31mnão\033[m formam um triângulo')

