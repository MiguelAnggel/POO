class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
#metodos:
    def comer(self):
        print(f'{self.nombre} esta comiendo')

    def dormir(self):
        print(f'{self.nombre} esta durmiendo')

    def hacer_sonido(self):
        print(f'{self.nombre} esta haciendo sonido')

    def __del__(self):
        print(f'{self.nombre} se ha ido al cielo de los animales')