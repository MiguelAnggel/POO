from ContadorPasos import ContadorPasos

#esto es un ejemplo de una funcion
def main():
   micontador = ContadorPasos(5)
   print(micontador.pasos)

   distancia1 = int(input("¿que distancia vas a caminar? "))
   pasos1= micontador.calcularPasos(distancia1)
   print("para caminar", distancia1, "metros, se ocupan", pasos1, "pasos" )
   
   for i in range(0, pasos1):
      micontador.contar()

      print(micontador.pasos)

      micontador.contar(5)

      print(micontador.pasos)

      micontador.contar(7,2)
      print(micontador.pasos)

   #pasos2= int(input("pasos? "))
   #distancia2= micontador.calcularDistancia(pasos2)
   #print("caminar", pasos2, "pasos, nos permite avanzar", distancia2, "metros")

print ("EJEMPLO SOBRECARGA DE OPERADORES")
cuenta1 = ContadorPasos(10)
cuenta2 = ContadorPasos(20)
cuenta3 = cuenta1 + cuenta2
cuenta2 = cuenta2 - cuenta1

print(cuenta3) 
print(cuenta2) 


if __name__ == "__main__":
   main()

