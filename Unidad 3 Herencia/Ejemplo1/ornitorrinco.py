from oviparo import Oviparo
from mamifero import Mamifero
from venenoso import Venenoso

class Ornitorrinco(Mamifero, Oviparo, Venenoso):
    
    def __init__(self, nombre, edad):
        #super().__init__(nombre, edad)   #Constructor de su clase padre 
        self.NUMERO_HUEVOS = 0
