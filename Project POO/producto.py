import json
#class Producto es la clase principal
class Producto:
    def __init__(self, sku, nombre, marca, presentacion, unidad_medida, precio_unitario, unidades_disponibles):
        self.sku = sku
        self.nombre = nombre
        self.marca = marca
        self.presentacion = presentacion
        self.unidad_medida = unidad_medida
        self.precio_unitario = precio_unitario
        self.unidades_disponibles = unidades_disponibles

#to_dict sirve para crear un diccionario, se hace serializacion que 
# es el proceso de convertir en un formato que se pueda almacenar.
    def to_dict(self):
        return {
            "sku": self.sku,
            "nombre": self.nombre,
            "marca": self.marca,
            "presentacion": self.presentacion,
            "unidad_medida": self.unidad_medida,
            "precio_unitario": self.precio_unitario,
            "unidades_disponibles": self.unidades_disponibles
        }