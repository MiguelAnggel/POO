from minisplit import Minisplit

if __name__ == "__main__":

    marca = input("Ingresar la marca del Minisplit: ")
    modelo = input("Ingresar el modelo del Minisplit: ")
    
    #Objeto
    mi_minisplit = Minisplit(marca, modelo)

    #Menu de control
    while True:
        print("\t **** Menu ****")
        print("1. Encender/Apagar")
        print("2. Cambiar de Modo ")
        print("3. Subir la Temperatura")
        print("4. Bajar la Temperatura")
        print("5. Cambiar Velocidad del Ventilador")
        print("6. Activar/Desactivar Ventilador Movil")
        print("7. Informacion del minisplit")
        print("8. Salir")

        control = int (input("Ingrese el número de la operación que desea realizar: "))

        if control == 1:
            mi_minisplit.encender_apagar()
        elif control == 2:
            modo = int (input("Ingrese el nuevo modo (1. Frio, 2. Abanico, 3. Calefacción): "))
            if modo == 1:
                print("Esta en modo Bajo")
            elif modo == 2:
                print("Esta en modo Abanico")
            elif modo == 3:
                print("Esta en modo Calefaccion")
            else:
                print("Opcion no valida. Eliga otra")
            mi_minisplit.especificar_modo(modo)

        elif control == 3:
            mi_minisplit.subir_temperatura()
        elif control == 4:
            mi_minisplit.bajar_temperatura()
        elif control == 5:
            velocidad = int (input("Ingresar la velocidad del ventilador (1. Bajo, 2. Medio, 3. Alto): "))
            if velocidad == 1:
                print("Esta en modo BAJO")
            elif velocidad == 2:
                print("Esta en modo MEDIO")
            elif velocidad == 3:
                print("Esta en modo ALTO")
            else:
                print("Opcion no valida. Eliga otra")
            mi_minisplit.cambiar_velocidad_ventilador(velocidad)
        elif control == 6:
            mi_minisplit.activar_desactivar_ventilador_movil()
        elif control == 7:
            mi_minisplit.informacion_minisplit()
        elif control == 8:
            print("Gracias!")
            break
        else:
            print("Opcion no valida, seleccione otra opcion.")
