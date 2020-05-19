# for range
for i in range(10): 
    print(i)

convidados = ['João', 'Maria', 'José', 'Ana', 'Chico']

# for each
# Faz o loop até acessar todos os elemento do vetor
for convidado in convidados:
    print(convidado + ' está convidado')

# for range
# Faz o loop pelo tamanho do vetor/número, etc
for i in range(len(convidado)):
    convidado = convidados[i]
    print(convidado + ' está convidado (for range)')


saida = True
contador = 0

# while - enquanto
# Faz o loop enquanto uma condição for verdadeira
# while saida:
#     contador = contador + 1
#     if contador == 5:
#         saida = False
    
#     print('While contador ' + str(contador))

while contador > 5:
    contador = contador + 1
    print('While contador ' + str(contador))

