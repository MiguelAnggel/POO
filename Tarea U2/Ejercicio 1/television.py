class Television:
    #Constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.canal = 1
        self.volumen = 30
        self.encendida = False
        self.silencio = False
        self.volumen_previo = None

    #Metodos del ejercicio
    def encender_apagar(self):
        self.encendida = not self.encendida
        if self.encendida:
            print("El televisor esta encendido.")
        else:
            print("El televisor esta apagada.")

    def especificar_canal(self, canal):
        if self.encendida:
            if canal > 0:
                self.canal = canal
                print(f"Se ha cambiado al canal {canal}.")
            else:
                print("El numero de canal debe ser mayor que cero.")
        else:
            print("El televisor esta apagado, Enciendelo.")

    def subir_canal(self):
        if self.encendida:
            self.canal += 1
            print(f"Se ha cambiado al canal {self.canal}.")
        else:
            print("El televisor esta apagado, Enciendelo.")

    def bajar_canal(self):
        if self.encendida:
            if self.canal > 1:
                self.canal -= 1
                print(f"Se ha cambiado al canal {self.canal}.")
            else:
                print("Estas en el canal mas bajo.")
        else:
            print("El televisor est apagado, Enciendelo.")

    def subir_volumen(self):
        if self.encendida:
            if self.volumen < 100:
                self.volumen += 1
                print(f"El volumen ha aumentado a {self.volumen}.")
            else:
                print("El volumen esta en el nivel maximo.")
        else:
            print("El televisor esta apagadado, Enciendelo.")

    def bajar_volumen(self):
        if self.encendida:
            if self.volumen > 0:
                self.volumen -= 1
                print(f"Volumen disminuido a {self.volumen}.")
            else:
                print("El volumen esta en el nivel minimo.")
        else:
            print("El televisor esta apagadado, Enciendelo.")

    def especificar_volumen(self, volumen):
        if self.encendida:
            if 0 <= volumen <= 100:
                self.volumen = volumen
                print(f"Volumen establecido en {self.volumen}.")
            else:
                print("El volumen debe estar en un rango de 1 a 100.")
        else:
            print("El televisor esta apagadado, Enciendelo.")

    def silenciar(self):
        if self.encendida:
            if not self.silencio:
                self.volumen_previo = self.volumen
                self.volumen = 0
                self.silencio = True
                print("La televisión está en modo silencio.")
            else:
                print("La televisión ya está en modo silencio.")
        else:
            print("El televisor esta apagadado, Enciendelo.")

    def quitar_silencio(self):
        if self.encendida:
            if self.silencio:
                if self.volumen_previo is not None:
                    self.volumen = self.volumen_previo
                    self.volumen_previo = None
                    self.silencio = False
                    print(f"Se ha quitado el modo silencio. Volumen: {self.volumen}.")
            else:
                print("La televisión no está en modo silencio.")
        else:
            print("El televisor esta apagadado, Enciendelo.")

    def informacion_televisor(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Canal actual: {self.canal}")
        print(f"Volumen actual: {self.volumen}")
        if self.silencio:
            print("Modo silencio activado.")
