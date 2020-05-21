# Criando uma class
class Animal:
    # Definindo um método, quando não há argumento
    #  ele recebe ele mesmo(self)
    def fazer_barulho(self):
        print('Barulho de animal')

class Domestico:
    def esta_dormindo(self):
        return True

# Extendendo de uma classe
# classe_filha(classe_mae)
class Mamifero(Animal):
    pass

# Herança multiplas
class Cachorro(Animal, Domestico):
    # É póssivel classes filhas terem métodos próprios
    def enterrar_osso(self):
        print('O osso foi enterrado')

class Gato(Animal):
    # Classe filhas podem reescrever um método herdado da classe mãe
    def fazer_barulho(self):
        print('Miau...Miau')

gato = Gato()

gato.fazer_barulho()

cachorro = Cachorro()

cachorro.fazer_barulho()
print(cachorro.esta_dormindo())
cachorro.enterrar_osso()
