var1 = input('Digite algo: ')
print('\033[1;34;43mO tipo primitivo é {}\033[m'.format(type(var1)))
print('\033[1;35;43mO valor digitado é númerico?', var1.isnumeric(), '\033[m')
print('\033[1;30;44mO valor digitado é letra?', var1.isalpha(), '\033[m')
print('\033[1;32;44mO valor digitado é alfanumérico?', var1.isalnum(), '\033[m')
print('\033[7;36mO valor digitado são letras maisculas?', var1.isupper(), '\033[m')
print('\033[7;36mO valor digitado são letras minusculas?', var1.islower(), '\033[m')
