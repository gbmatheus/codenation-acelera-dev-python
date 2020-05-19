nome = 'Eu' # str - String
idade = 24 # int - Integer
altura = 1.69 # float
tutor = False # bool - Boolean
trabalhando = None # None - vazio

# print - cmd para imprimir
print(nome)
print(idade)
print(altura)
print(tutor)
print(trabalhando)

# Adição
nova_idade = idade + 30

# Concatenação
nome_cidade = nome + ' Serra Talhada'

print(nova_idade)
print(nome_cidade)

altura_sem_tenis = altura - 5.0

print(altura_sem_tenis)

# Concatenação (str + float ou int) tipos não são compatíveis
# resultado = nome + idade
resultado = idade + altura

print(resultado)