def main():
    print("miguel angel montoya cruz")
    #en python no se ponen los tipos de datos
    #la funcion int funciona para convertir a entero 
    edad = int(input("cuantos años tienes? ")) #esto es una variable 

    if edad >= 20:
        print("buenos dias")
    else:
        print("que onda")
    
    limite = 11
    x = 0
#Lo de abajo es para crear un contador
    for x in range(0, limite):
        print(x)

#esto es un arreglo dinamico  
    for x in ["a", "b", "c", "d"]:
        print(x)

#esto es un while, no existe el do while
    x = 0
    while x < 10:
        print(x+1)
        x+=1

    nombres = ["jaime", "rigo", "spike", "daniel"]
    print(nombres)
    #nombres.append (input("Dame tu nombre: "))
    #nombres.insert(2, input("dame tu nombre:"))

    print(nombres)

    #print(nombres[3])

if __name__ == "__main__":
    main()