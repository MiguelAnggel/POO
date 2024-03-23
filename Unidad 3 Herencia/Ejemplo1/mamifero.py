from animal import Animal
class Mamifero(Animal):

    def __init__(self, nombre, edad, especie = "Mamifero"):
        super().__init__(nombre, edad)  #constructor de la clase Animal
        self.especie = especie

    def amamantar(self):  #importar la clase animal
        print(" amamantar 🍼")

    def parir(self):
        print("👶")