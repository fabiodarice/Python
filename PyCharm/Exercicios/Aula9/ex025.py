nome = str(input('\033[34;43mDigite o nome completo:\033[m ')).strip().title()
print('O nome digitado tem o sobrenome "Silva"?: {}'.format('Silva' in nome))