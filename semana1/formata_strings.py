idade = 24

# print('Minha idade é: ' + idade)
print('Minha idade é: ' + str(idade))

# formataão
print('Minha idade é: {}'.format(idade))

# f-String
# f'txt' recurso novo da para formatação da string, parecido com o template string
print(f'Minha idade é: {idade}')

nome = 'Gabriel 22222213asdas1222222222222222asdamsdasmdkas222222222222kdmasd'

# Limitando a quantidade de caracteres
# {variavel:.x} a exibiçao será de apenas quantidade de x de caracteres a serem exibidos
# {variavel:0x} a exibição será completada por 0 na quantidade de x números
print(f'Meu nome é: {nome:.7} e eu tenho {idade:05} anos')

dinheiro = 2.5

# {variavel:.xf} utilizado para exibir uma quantidade x de casas decimais
print(f'Eu tenho {dinheiro:.2f} R$')

lista_itens = ['Garfo', 'Faca', 'Copo', 'Prato']

print(f'Eu almoço com {lista_itens[0]} e {lista_itens[1]} no {lista_itens[-1]}')

# É possível fazer operações dentro das chaves
print(f'Eu terei {idade + 30} anos daqui a 30 anos')