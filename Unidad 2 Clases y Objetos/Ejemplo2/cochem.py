class Coche:
    def __init__(self):
        self.llantas = []

    def encender(slef, motor): # este metodo recibe como paramytro un motor
        motor.encender()

    def agregarLlanta(self, llanta): #metodo que recibe como parametro un objeto de tipo llanta
        self.llantas.append(llanta)# metodo append es para agregarlo a la lista