class Mamifero:
    def emitir_som(self):
        pass

class Cachorro(Mamifero):
    # É póssivel fazer a reescrita da métodos da classe Pai
    # Com seus próprios comportamentos
    def emitir_som(self):
        print('au au')

class Gato(Mamifero):
    def emitir_som(self):
        print('miau miau')

class Rato(Mamifero):
    def emitir_som(self):
        print('zzzzzzz')

cachorro = Cachorro()
gato = Gato()
rato = Rato()

mamiferos = [cachorro, gato, rato]

# Pode chamar métodos que foram reescritos a partir de um objeto do tipo pai
for mamifero in mamiferos:
    mamifero.emitir_som()