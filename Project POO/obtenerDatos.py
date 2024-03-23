from producto import Producto
def datos_producto():
    #Manejo de excepciones para la vairable sku 
    while True:
        try: 
            sku = int(input("Ingrese el SKU del producto: "))
            break
        except ValueError:
            print("Debes ingresar un número entero. Intenta de nuevo.")
        
    nombre = input("Ingrese el nombre del producto: ")
    marca = input("Ingrese la marca del producto: ")
    presentacion = input("Ingrese la presentación del producto(bolsa, caja, botella, unidad): ")
    unidad_medida = input("Ingrese la unidad de medida del producto(kg, l, mil, gr): ")
    #Manejo de excepciones para la vairable precio_unitario
    while True:
        try:
            precio_unitario = int(input("Ingrese el precio unitario del producto: "))
            break
        except ValueError:
            print("Debes ingresar un número entero. Intenta de nuevo.")
    #Manejo de excepciones para la vairable unidades_disponibles
    while True:
        try:
            unidades_disponibles = int(input("Ingrese las unidades disponibles del producto: "))
            break
        except ValueError:
            print("Debes ingresar un número entero. Intenta de nuevo.")

    return Producto(sku, nombre, marca, presentacion, unidad_medida, precio_unitario, unidades_disponibles)