from animal import Animal
class Gato(Animal):
    #constructor con parametros para gato:
    def __init__(self, nombre, edad, vidas):
        super().__init__(nombre, edad) #LLamada explicita
        self.vidas = vidas  #Vidas parametro propio de la clase Gato

    def hacer_sonido(self):
        super().hacer_sonido()
        print("miauuu 🐈")
        #print(f'{self.nombre} esta maullando') #metodo unico para gato

    def sobrevive(self):
        if self.edad > 15 and self.vidas > 1:
            self.vidas -= 1
            self.edad = 1
        return self.vidas > 0
    
    def __del__(self): #destructor de la clase gato
        print(f'{self.nombre} se ha ido al cielo de los gatos')