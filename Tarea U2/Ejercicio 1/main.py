from television import Television

if __name__ == "__main__":
    
    marca = input("Ingresar marca del televisor: ")
    modelo = input("Ingresr modelo del televisor: ")
    mi_televisor = Television(marca, modelo)


    #Menu de control
    while True:
        print("\t **** Menu ****")
        print("1. Encender/Apagar")
        print("2. Especificar Canal")
        print("3. Subir de Canal")
        print("4. Bajar de Canal")
        print("5. Subir de Volumen")
        print("6. Bajar de Volumen")
        print("7. Especificar Volumen")
        print("8. Silenciar/Quitar Silencio")
        print("9. Informacion del televisor")
        print("10. Salir")


        control = int (input("Ingresar el numero de la operacion que realizara: "))

        if control == 1:
            mi_televisor.encender_apagar()
        elif control == 2:
            canal = int(input("Ingrese el número de canal: "))
            mi_televisor.especificar_canal(canal)
        elif control == 3:
            mi_televisor.subir_canal()
        elif control == 4:
            mi_televisor.bajar_canal()
        elif control == 5:
            mi_televisor.subir_volumen()
        elif control == 6:
            mi_televisor.bajar_volumen()
        elif control == 7:
            volumen = int(input("Ingrese el nivel de volumen (0-100): "))
            mi_televisor.especificar_volumen(volumen)
        elif control == 8:
            if mi_televisor.muted:
                mi_televisor.quitar_silencio()
            else:
                mi_televisor.silenciar()
        elif control == 9:
            mi_televisor.informacion_televisor()
        elif control == 10:
            print("Gracias!")
            break
        else:
            print("Opcion no valida. seleccione una opcion valida.")
