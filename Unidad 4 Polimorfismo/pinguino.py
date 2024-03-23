from animal import Animal
from oviparo import Oviparo

class Pinguino(Animal, Oviparo):
    def comer(self):
        print("El pinguino esra comiendo 🦪")