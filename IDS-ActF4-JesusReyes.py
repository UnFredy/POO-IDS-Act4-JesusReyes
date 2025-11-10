
# CLASE PRINCIPAL: Producto

class Producto:
    
    __limite_descuento = 0.5
    
    def __init__(self, nombre, descripcion, precio, stock):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        print(f"Nombre del producto: {self.nombre}.\nDescripción: {self.descripcion}. \nPrecio: ${self.precio} \nStock: {self.stock}.")
    
    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"Stock actualizado a: {self.stock} unidades.")
        
    def mostrar_precio(self):
        print(f"${self.precio}") 
    
    def venta(self, cantidad):
        
        if self.stock > 0:
            if self.stock - cantidad >= 0:
                self.stock -= cantidad
                print(f"Venta realizada! Nuevo stock: {self.stock}")
            else:
                print(f"Stock insuficiente para la venta. Stock actual: {self.stock}")
        else:
            print("No hay stock")
    
    def aplicar_descuento(self, descuento):
        
        if descuento > self.__limite_descuento:
            raise ValueError("Descuento mayor al limite")
        self.precio = round(self.precio * (1 - descuento), 2)
    
    def __str__(self):
        return f"Nombre del producto: {self.nombre}.\nDescripción: {self.descripcion}. \nPrecio: ${self.precio} \nStock: {self.stock}."

class Electronico(Producto):
    pass

class Ropa(Producto):
    pass

class Alimento(Producto):
    pass

class Higiene(Producto):
    pass

class Videojuegos(Electronico):
    pass
    
Tele = Producto("Tele", "Televisor 42 pulgadas", 5500, 10)


print(Tele)
Tele.aplicar_descuento(0.3)
Tele.actualizar_stock(20)
Tele.mostrar_info()