from multipledispatch import dispatch

class ContadorPasos:
    pasos = 0

    def __init__(self, pasos):  # creamos el constructor
        self.pasos = pasos

#EJEMPLOS DE MOTODOS MAGICOS SOBRECARGADOS
    def __add__(self, cuenta): #operador de suma 
        return ContadorPasos(self.pasos + cuenta.pasos)
    
    def __sub__(self, cuenta): #operador de resta
        return ContadorPasos(self.pasos - cuenta.pasos)
    
    def getpasos(self):
        return self.pasos
    
    def __string__(self):
        return str(self.pasos) +"pasos" 

    #definnir nuestro constructor:
    def __init__(self, pasos=0):
        self.pasos = pasos

    #esto es un destructor:     se utiliza para el cierre de memoria
    def __del__ (self):
        pass # si yo pongo esto es una funcion vacia
        # print("Termine con ", self.pasos)


    @dispatch() #metodo sin parametros
    def contar(self):
        self.pasos += 1
        
    @dispatch(int)# metodo con un parametro de tipo entero
    def contar(self, pasos):
        self.pasos += pasos

    @dispatch(int, int)#metodo con dos parametros de tipo entero
    def contar(self, pasos, saltos):
        self.pasos += pasos + (2*saltos)

    def saltarAdelante(self):
        self.contar()
        self.contar()

#toma la cantidad de pasos y devuelve la cantidad de pasos
    def calcularDistancia(self, pasos):
        # 1 m = 0.7 pasos
        return pasos * 0.7 #esto es una funcion con retorno
    
    def calcularPasos(self, distancia):
        return round(distancia / 0.7) #funcion con retorno