lista_convidados = ['José', 'Maria', 'João', 'Chico']

print(lista_convidados)

# Lista é mutável
# Adição de um item
lista_convidados.append('Ana')

print(lista_convidados)

# Remoção de um item
lista_convidados.remove('José')
print(lista_convidados)

# Primeiro item está no indice 0
print(lista_convidados[0])

print(lista_convidados[3])
# Accesso ao ultimo item
print(lista_convidados[-1])

# É possível adicionar outras tipo em um lista
#  mas não é recomendado, se pode ter um nix de valores
lista_convidados.append(20)

print(lista_convidados)

# Tupla tuple
# É um tipo de lista imutável
tupla1 = (1,2,3)
tupla2 = (4, 5, 6)

print(tupla1)

# Não há o método de adicionar valores
# tupla.append

# Tem acesso mais rápido, pois são imutáveis
# Vatangem: Para leitura de dados
# Desv.: Para adição de novos valores

# É possível fazer união de tuplas
tupla3 = tupla1 + tupla2

print(tupla3)

# Dicionario mapeamento de (chave: valor)
#  Parecido com o json

dados_pessoais = {'nome': 'Batman', 'cidade': 'Gothan'}

print(dados_pessoais)

# adicionando valor
dados_pessoais['veiculo'] = 'Batmovel'

print(dados_pessoais)

# del exclui o contéudo de uma váriavel
del dados_pessoais['cidade']

print(dados_pessoais)

