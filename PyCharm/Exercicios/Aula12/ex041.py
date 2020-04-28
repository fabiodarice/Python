# Importação de bibliotecas
from datetime import date

# Título do programa
print('\033[1;34;40mCLASSIFICAÇÃO DE CATEGORIAS PARA NATAÇÃO\033[m')

# Objetos
nascimento = int(input('\033[30mDigite o ano do seu nascimento:\033[m '))
idade = date.today().year - nascimento
mirim = 9
infantil = 14
junior = 19
senior = 20

# Lógica
if idade <= mirim:
    print('Sua idade é \033[1;33m{} anos\033[m, e sua categoria é a \033[1;34mMIRIM!\033[m'.format(idade))
elif idade <= infantil:
    print('Sua idade é \033[1;33m{}\033[m anos, e sua categoria é a \033[1;34mINFANTIL!\033[m'.format(idade))
elif idade <= junior:
    print('Sua idade é \033[1;33m{}\033[m anos, e sua categoria é a \033[1;34mJUNIOR!\033[m'.format(idade))
elif idade <= senior:
    print('Sua idade é \033[1;33m{}\033[m anos, e sua categoria é a \033[1;34mSÊNIOR!\033[m'.format(idade))
elif idade > senior:
    print('Sua idade é \033[1;33m{}\033[m anos, e sua categoria é \033[1;34mMASTER!\033[m'.format(idade))