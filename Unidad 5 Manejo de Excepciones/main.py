def main():
    ''' 
    repite = True
    while repite:
        try:
            a = int(input("Ingresa el valor A: "))
            b = int(input("Ingresa el valor B: "))
        except ValueError:
                print("Losa valores A y B , deben ser enteros")
        else:
            repite = False
        #exit()
    '''

    a= leeEnteros("Ingresa el numero A: ")
    b= leeEnteros("Ingresa el numero B: ")

    repite = True
    while repite:
        try:
            print(divide(a,b))
            break    #linea agregada por mi, ya que se imprimia el numero sin parar
        except ZeroDivisionError:
            print("No se pùede dividir entre cero")
            while b == 0:
                b = leeEnteros("Ingrese el numero B: ")
                print(divide(a,b))    #Linea agregada por mi
            else: 
                repite = False
    
def divide(a,b):
    # throws ZeroDivisionError
    return a / b

def leeEnteros(etiqueta):
    repite = True
    while repite:
        try:
            x = int(input(etiqueta))
        except ValueError:
            print("El valor debe se entero")
        else:
            repite = False
            return x
    
if __name__ == '__main__':
    main()
