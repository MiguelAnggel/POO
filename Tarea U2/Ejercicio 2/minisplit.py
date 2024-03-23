class Minisplit:

    #Constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.modo = "Frio"  
        self.temperatura = 25  
        self.velocidad_ventilador = "Bajo"  
        self.ventilador_movil_activado = False

    #Metodos del ejercicio
    def encender_apagar(self):
        self.encendido = not self.encendido
        if self.encendido:
            print(f"{self.marca} {self.modelo} esta encendido.")
        else:
            print(f"{self.marca} {self.modelo} esta apagado.")


    def especificar_modo(self, modo):
        if self.encendido:
            modos_validos = [1, "Frio",  2, "Abanico", 3, "Calefacción"]
            if modo in modos_validos:
                self.modo = modo
                print(f"Modo cambiado a {modo}.")
            else:
                print("Modo no valido. Los modos validos son: Frio, Abanico, Calefacción.")
        else:
            print("El Minisplit esta apagado. Enciendelo primero.")

    def subir_temperatura(self):
        if self.encendido:
            if self.temperatura < 35:
                self.temperatura += 1
                print(f"Temperatura aumentada a {self.temperatura} grados Celsius.")
            else:
                print("La temperatura se encuentra en el nivel maximo.")
        else:
            print("El Minisplit esta apagado. Enciendelo primero.")

    def bajar_temperatura(self):
        if self.encendido:
            if self.temperatura > 18:
                self.temperatura -= 1
                print(f"Temperatura disminuida a {self.temperatura} grados Celsius.")
            else:
                print("La temperatura se encuentra en el nivel minimo.")
        else:
            print("El Minisplit esta apagado. Enciendelo primero.")

    def cambiar_velocidad_ventilador(self, velocidad):
        if self.encendido:
            velocidades_validas = [1, "Bajo", 2, "Medio", 3, "Alto"]
            if velocidad in velocidades_validas:
                self.velocidad_ventilador = velocidad
                print(f"Velocidad del ventilador cambiada a {velocidad}.")
            else:
                print("Velocidad no valida. Las velocidades validas son: Bajo, Medio, Alto.")
        else:
            print("El Minisplit esta apagado. Enciendelo primero.")

    def activar_desactivar_ventilador_movil(self):
        if self.encendido:
            self.ventilador_movil_activado = not self.ventilador_movil_activado
            if self.ventilador_movil_activado:
                print("El ventilador movil esta activado.")
            else:
                print("El ventilador movil esta desactivado.")
        else:
            print("El Minisplit esta apagado. Enciendelo primero.")

    def informacion_minisplit(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"{self.marca} {self.modelo} - Estado: {estado}")
        print(f"Modo: {self.modo}")
        print(f"Temperatura actual: {self.temperatura} grados ")
        print(f"Velocidad del ventilador: {self.velocidad_ventilador}")
        if self.ventilador_movil_activado:
            print("El entilador movil esta activado.")
        else:
            print("El ventilador movil esta desactivado.")
