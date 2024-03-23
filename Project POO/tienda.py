import json
from producto import Producto
class Tienda:
    def __init__(self):
        self.productos = []

    #Modulo para cargar datos(productos) en Json
    def cargar_productos(self):
        try:
            with open("productos.json", "r") as archivo:
                productos_data = json.load(archivo)
                self.productos = [Producto(**producto) for producto in productos_data]
        except FileNotFoundError:
            self.guardar_productos()

    #Modulo para guardar datos(productos) en Json
    def guardar_productos(self):
        with open("productos.json", "w") as archivo:
            json.dump([producto.to_dict() for producto in self.productos], archivo, indent=2)

    #Modulo para agregar productos a la tienda
    def agregarProducto(self, producto):
        self.productos.append(producto)
        self.guardar_productos()

    #Modulo para editar producto
    def editarProducto(self, sku, nuevo_nombre, nueva_cantidad, nuevo_precio):
        for producto in self.productos:
            if producto.sku == sku:
                producto.nombre = nuevo_nombre
                producto.unidades_disponibles = nueva_cantidad
                producto.precio_unitario = nuevo_precio
                self.guardar_productos()
                break
            '''elif producto.sku != sku: #edhasta abajo
                producto.nombre = nuevo_nombre
                producto.unidades_disponibles = nueva_cantidad
                producto.precio_unitario = nuevo_precio
                self.productos.append(producto)
                self.guardar_productos()'''
        else:
            print("Producto no encontrado")

    #Modulo para listar productos agregados a la tienda
    def listarProductos(self):
        for producto in self.productos:
            if producto.unidades_disponibles > 0:
                print(f"sKU: {producto.sku}, nombre: {producto.nombre}, Cantdisponible: {producto.unidades_disponibles}, Precio: ${producto.precio_unitario}")

    #Modulo para borrar producto
    def borrarProducto(self, sku):
        self.productos = [producto for producto in self.productos if producto.sku != sku]
        self.guardar_productos()

    #Modulo  para buscar producto
    def buscarProducto(self, nombre, sku):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto

            elif producto.sku == sku:
                return producto
        return None
    
    # Modulo para la venta de productos
    def ventaProductos(self, items): # items en Este metodo devuelve una vista de los pares clave-valor del diccionario como listas
        total_venta = 0              #Para usar la función items en Python, primero debe tener un objeto diccionario. Luego, puede llamar al método items en el objeto diccionario. El método items devolverá una lista
        for sku, cantidad in items.items():
            producto = self.buscarProducto(sku)
            if producto:
                if producto.unidades_disponibles >= cantidad:
                    producto.unidades_disponibles -= cantidad
                    total_venta += cantidad * producto.precio_unitario
                else:
                    print(f"No hay suficientes productos para vender {cantidad} unidades de {sku}.")
            else:
                print(f"Producto SKU {sku} no encontrado.")

        if total_venta > 0:
            self.guardar_productos()
            print(f"Venta realizada correctamente. Total: ${total_venta}")
        else:
            print("No hay venta realizada.")
