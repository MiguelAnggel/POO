def main ():
    edades = [] #variable edad la definimos como un Arreglo

    for i in range(0,10):
        edad = int (input("Edad: "))
        #lo de abajo es un metodo para agregar
        edades.append(edad)#append para agregar elementos a un arreglo

#la funcion sort ordena de mayor a menor   
    print(edades.sort)

if __name__ == "__main__":
    main()