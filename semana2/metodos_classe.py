class Impressora:
    def __init__(self):
        self.a = 10

    # Não se utiliza o self
    # E se utiliza o 'cls' ao invés do 'class', class é palavra reservada
    @classmethod # método de class, é preciso da notação @classmethod
    def imprimir_folha(cls):
        print('folha impressa')

    @classmethod
    def imprimir_livro(cls, paginas):
        for i in range(paginas):
            cls.imprimir_folha()

    @classmethod
    def imprimir_a(cls):
        print(cls.a)

# Não é preciso instaciar para faze a chamada de class method
# Pode ser chamado a partir da classe
Impressora.imprimir_folha()

print("Imprimindo")
Impressora.imprimir_livro(5)

impressora = Impressora()

impressora.imprimir_folha()

print('Impressora A')
# class method não tem acesso ao atributos definidos no escopo da instância
# Impressora.imprimir_a()
impressora.imprimir_a()