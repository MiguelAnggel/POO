from abc import ABC, abstractmethod   #libreria para la abstraccion
from mixinMortalidad import MixinMortalidad

class Animal (ABC, MixinMortalidad):

    #constructor de la clase animal (no importa mucho si lo agregamos ya que es clase abstracta),
    #pero en este caso lo agregamos
    def __init__(self, nombre="", edad=1, especie= "mamifero"):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod #metodo abstracto 
    def comer(self):
        pass

    def dormir(self): #metodo normal que se va a heredar a otras clases
        if self.nombre == "  ":
            print(f'el animal esta durmiendo 💤')
        else:
            print(f'{self.nombre} esta durmiendo 💤')

    