class Cliente:
    def __init__ (self, nome, documento):
        self.nome = nome
        self.documento = documento

class Produto:
    def __init__ (self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoCompras:
    # Para o objeto existir, é preciso que os objetos que o compoem existam
    def __init__ (self, cliente, produtos):
        self.num_pedido = '123'
        self.produtos = produtos
        self.cliente = cliente

    # Notação para chamar uma função como atributo
    @property
    def valor_carrinho (self):
        total = 0.0
        for produto in produtos:
            total += produto.preco
        
        return total
    
    def adicionar_produto (self, produto):
        self.produtos.append(produto)
    
    def remover_produto (self, produto):
        self.produtos.remove(produto)
    
    def fechar_carrinho (self):
        print(f'Fechando o pedido {self.num_pedido}')
        print(f'Valor do carrinho {self.valor_carrinho}')
        print(f'Nome do cliente {self.cliente.nome}')
        print('Obg pela compra')

cliente = Cliente('Gabriel', '12345')

tv = Produto('tv', 1000.90 )
maquina_de_cafe = Produto('maquina de café', 89.80 )

produtos = [tv, maquina_de_cafe]

# Compondo o objeto, e adicionando os objetos que ele depende na instância
carrinho = CarrinhoCompras(cliente, produtos)

teclado = Produto('teclado', 175.20)

carrinho.adicionar_produto(teclado)

carrinho.remover_produto(tv)

print(carrinho.valor_carrinho)
carrinho.fechar_carrinho()