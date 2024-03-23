from animal import Animal
from mamifero import Mamifero
from oviparo import Oviparo

class Zoologico:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal:Animal):  #para forzar a que sea del tipo de dato animal
        self.animales.append(animal) # metodo para agragar animales

    def alimentar_animales(self): #metodo para alimentar animales 
        for animal in self.animales:
            animal.comer()
            if isinstance(animal, Mamifero): #si esta vairable es una subclase de tipo mamifero 
                animal.amamantar()

    def hora_dormir(self):
        for animal in self.animales:
            animal.dormir()

    def nacen_animales(self):
        for animal in self.animales:
            if isinstance(animal, Mamifero):
                animal.parir()
            else:
                animal.poner_huevos()
