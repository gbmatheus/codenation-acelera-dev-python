idade = 20

# Condicional se
if idade < 18:
    print("Menor de idade")
# Condicional se não
else: 
    print("Maior de idade")

veiculo1 = {'tipo': 'carro', 'marca': 'Fiat', 'potencia_motor': 140}
veiculo2 = {'tipo': 'moto', 'marca': 'Honda', 'potencia_motor': 140}

# Operadores lógico
# and - e - os valores devem ser verdadeiro para a condição ser verdadeira
# or - ou - um dos valores dever ser verdadeiro para a condição ser verdadeira
if veiculo2['tipo'] == 'moto' and veiculo2['marca'] == 'Honda':
    print("O veiculo é uma moto")
else:
    # print("O veiculo é  um carro")
    print("O veiculo não é uma moto")

# Atribuindo valor a partir de uma condição | True/False 
resultado = veiculo2['tipo'] == 'moto'
print(resultado)

if veiculo1['tipo'] == 'moto' or veiculo1['potencia_motor'] < 120:
    print("Você tem um veículo muito rápido")
else:
    print("Seu veículo não é rápido")

# If com and e or aninhados
if (veiculo2['tipo'] == 'carro' and veiculo2['potencia_motor'] > 120) or veiculo2['marca'] == 'Honda':
    print("O seu veículo é muito bom")

if veiculo2['tipo'] == 'moto':
    print("Moto")
# Elif - Se não, se
# No python não exite switch/case, então se usa elif no caso da verificação de varias condições
elif veiculo2['tipo'] == 'carror':
    print("Carro")
elif veiculo2['tipo'] == 'moto2':
    print('moto2')


condicao = [1,2,3]

# If a partir do contéudo da variável
if condicao:
    print("Verdadeiro")
else:
    print("Falso")

# len() - retorna o tamanho da variável
if len(condicao):
    print("Verdadeiro")
else:
    print("Falso")

print(len(condicao))





















