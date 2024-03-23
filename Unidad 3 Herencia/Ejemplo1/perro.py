from animal import Animal
class Perro(Animal):

    #constructor con parametros para perro:
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        super().hacer_sonido()
        print("woooff 🐕")
        #print(f'{self.nombre} esta ladrando') #metodo unico para perr¡

    def es_cachorro(self):
        return self.edad < 2
    
    def __del__(self): #destructor de la clase perro
        print(f'{self.nombre} se ha ido al cielo de los perros')
