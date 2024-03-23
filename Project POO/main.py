import json
from producto import Producto
from tienda import Tienda 
from obtenerDatos import datos_producto #hereda funcion datos_producto

#def main() modulo para realizar las ejecuciones del proyecto
def main():
    tiendita = Tienda() # Instancia de Tienda
    tiendita.cargar_productos() # carga los datos de productos guardados

    while True:
        opcion = mostrarMenu()
        opcion = int(input("ingrese una opcion: "))
        if opcion == 1: #opcion agregar
            nuevo_producto = datos_producto()
            tiendita.agregarProducto(nuevo_producto)
            print("Producto creado correctamente.")

        elif opcion == 2: #opcion editar
            sku = input("Ingrese SKU del producto a editar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            nuevo_precio = int(input("Ingrese el nuevo precio del producto: "))
            tiendita.editarProducto(sku, nuevo_nombre, nueva_cantidad, nuevo_precio)

            print("Producto editado correctamente.")

        elif opcion == 3: #opcion listar
            print("\n Lista de Productos: ")
            tiendita.listarProductos()

        elif opcion == 4: #opcion borrar
            sku = input("Ingrese SKU del producto a borrar: ")
            tiendita.borrarProducto(sku)
            print("Producto borrado correctamente.")

        elif opcion == 5:
            #opcion buscar
            nombre = input("Ingrese nombre del producto a buscar: ")
            sku = int(input("Ingrese el sku: "))
            producto_encontrado = tiendita.buscarProducto(nombre,sku)
            # producto_encontrado = tiendita.buscarProducto(sku)
            if producto_encontrado:
                print("\n Producto Disponible... ")
                print(f"SKU: {producto_encontrado.sku}")
                print(f"Nombre: {producto_encontrado.nombre}")
                print(f"Marca: {producto_encontrado.marca}")
                print(f"Presentación: {producto_encontrado.presentacion}")
                print(f"Unidad de Medida: {producto_encontrado.unidad_medida}")
                print(f"Precio Unitario: ${producto_encontrado.precio_unitario}")
                print(f"Unidades Disponibles: {producto_encontrado.unidades_disponibles}")
            else:
                print("Producto no encontrado.")

        elif opcion == 6: #opcion vender
            items = {}
            while True:
                sku = int(input("Ingrese SKU del producto (o 'x' para terminar la compra): "))
                if sku == "0":
                    break
                cantidad = int(input(f"Ingrese la cantidad a vender del producto {sku}: "))
                items[sku] = cantidad

            tiendita.ventaProductos(items)

        elif opcion == 7: #opcion salir
            tiendita.guardar_productos() # Guarda los datos de productos agregados al inventario, 
            print("saliendo...")
            break
        else:
            print("ingrese una opcion valida: ")

def mostrarMenu():
    print("\tMenu principal de la Tiendita")
    print("1. Agregar Producto")
    print("2. Editar Producto")
    print("3. Listar Productos")
    print("4. Borrar Producto")
    print("5. Buscar Producto")
    print("6. Vender ")
    print("7. Salir")

if __name__ == "__main__":
    main()