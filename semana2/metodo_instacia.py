# Tem o escopo de instancia, a instancia é o escopo da classe

class Impressora:
    modelo = "Epson"

    def __init__(self, numero_folhas):
        self.numero_folhas = numero_folhas
    
    # Funções padrões, com self como argumento
    def imprimir_folha(self):
        print('folha impressa')

    def imprimir_livro(self, paginas):
        if paginas <= self.numero_folhas:
            for i in range(paginas):
                self.imprimir_folha()
                self.numero_folhas - self.numero_folhas - 1

    @classmethod
    def print_modelo(cls):
        print(cls.modelo)

    def print_modelo_instancia(self):
        print(self.modelo)

impressora = Impressora(15)

impressora.imprimir_folha()

impressora.imprimir_livro(10)

Impressora.print_modelo()

# O escopo da classe é superior ao escopo da instancia,
#  a instancia herda todo o escopo da classe
impressora.print_modelo_instancia()

# Erro é preciso da instancia
# Impressora.print_modelo_instancia()