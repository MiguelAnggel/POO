from animal import Animal
from gato import Gato
from perro import Perro 
from leon import Leon
from ornitorrinco import Ornitorrinco
from zoologico import Zoologico
from pinguino import Pinguino
def main():

    #objetos (instancias)
    lomito = Perro(nombre="oddie")
    michi = Gato(nombre="garfiel")
    alex = Leon(nombre="alex")
    perry = Ornitorrinco(nombre="perry")
    kovalski = Pinguino(nombre="kovalski")
    #animal = Animal()  #no se puede crear objetos(instanciar) de clases abstractas

    lomito.comer() #el perro esta comiendo...
    michi.comer()  #el gato esta comiendo
    lomito.dormir() #oddie esta durmiendo
    michi.dormir()  #garfiel esta durmiendo
    
    print("== EJEMPLO ==")
    #  uso de polimorfimo (cuando un contenedor puede almacenar diferentes objetos del mismo tipo)
    # lo de abajo puede ser variable polimorfica  y contine un arreglo
    animales = [lomito, michi, alex, perry] # arreglo
    #print(animales)

    for animal in animales:
        animal.comer()  # metodo sobreescrito
        animal.dormir() # metodo Heredado
        animal.morir() #metodo del mixin
    #perry.morir()

    # a partir de aqui vimos la composicion de clases
    print("==ZOOO==")
    #instanciamos el objeto zoo
    zoo = Zoologico()

    zoo.agregar_animal(lomito)
    zoo.agregar_animal(michi)
    zoo.agregar_animal(alex)
    zoo.agregar_animal(perry)
    zoo.agregar_animal(kovalski)

    zoo.alimentar_animales()
    zoo.hora_dormir()
    zoo.nacen_animales()

if __name__ == "__main__":
    main()