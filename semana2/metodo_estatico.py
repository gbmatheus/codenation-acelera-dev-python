# méto declarado na classe com escopo próprio
# notação staticmethod

class Impressora:
    
    @staticmethod
    def ligar_para_suporte():
        print("Liguei para o suporte")

    # é possivel fazer chamada de métodos estaticos
    # por métodos da classe e por métodos da instância
    
    @classmethod
    def deu_problema_na_impressora(cls):
        print('Analisando problema')
        cls.ligar_para_suporte()

    # é possível fazer chamada de métodos de classe
    #  a partir de métodos de instancia
    def imprimir(self):
        print("Imprimindo página 1")
        self.ligar_para_suporte()
        # self.deu_problema_na_impressora()


Impressora.ligar_para_suporte()

Impressora.deu_problema_na_impressora()

impressora = Impressora()

impressora.imprimir()