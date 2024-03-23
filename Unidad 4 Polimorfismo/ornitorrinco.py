from oviparo import Oviparo
from mamifero import Mamifero

class Ornitorrinco(Mamifero, Oviparo):
    
    def __init__(self, nombre="", edad=1):
        super().__init__(nombre, edad)   #Constructor de su clase padre 
        self.NUMERO_HUEVOS = 0

    def comer(self):
        print("EL ornitorrinco esta comiendo🍀🌾")

    def morir(self):
        print("oh!  me muero! :(")