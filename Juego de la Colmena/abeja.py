#Class Abeja clase principal
class Abeja:
    #Constructor 
    def __init__(self):
        self.ataque = 0
        self.simbolo = ""
        self.visitado = False

    #Metodo que devolvera verdadero true "Reina" solo si la abeja es reina
    def esReina(self):
        return False
    