valor = input('Digite algo: ')
print(f'Você digitou: {valor}')
print()
print(f'O tipo primitivo deste valor é: {type(valor)}')
print(f'Só tem espaços? {valor.isspace()}')
print(f'É um número? - {valor.isnumeric()}')
print(f'É alfabético? - {valor.isalpha()}')
print(f'É alfanumérico? - {valor.isalnum()}')
print(f'Está em maiúsculas? - {valor.isupper()}')
print(f'Está em miúsculas? - {valor.islower()}')
print(f'Está capitalizado? - {valor.istitle()}')
