# ===========================================================
# Proyecto: Sistema de gestión de inventarios
# Descripción: Ejemplo de polimorfismo, abstracción y herencia
# ===========================================================


from abc import ABC, abstractmethod


# ===========================================================
# CLASE ABSTRACTA PRINCIPAL: Producto

# Representa la estructura base para cualquier tipo de producto.
# Incluye atributos y métodos comunes que las subclases heredarán.
# ===========================================================
class Producto(ABC):
    
    __limite_descuento = 0.5    # Atributo privado: descuento máximo permitido (50%)
    
    def __init__(self, nombre, descripcion, precio, stock):
        """
        Constructor base para inicializar los atributos comunes a todos los productos.

        Parámetros:
        - nombre (str): nombre del producto.
        - descripcion (str): breve descripción del producto.
        - precio (float): precio actual del producto.
        - stock (int): cantidad disponible en inventario.
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
    
    # -------------------------------------------------------
    # MÉTODO ABSTRACTO
    # Cada subclase debe implementar su propia versión de este método.
    # -------------------------------------------------------
    @abstractmethod
    def mostrar_info(self):
        pass
    
    # -------------------------------------------------------
    # MÉTODOS COMUNES PARA TODAS LAS SUBCLASES
    # -------------------------------------------------------
    def actualizar_stock(self, cantidad):
        """
        Aumenta el stock actual del producto.

        Parámetros:
        - cantidad (int): número de unidades a añadir al inventario.
        """
        self.stock += cantidad
        print(f"{self.nombre}. Stock actualizado a: {self.stock} unidades.")
        
    def mostrar_precio(self):
        """Imprime el precio actual del producto."""
        print(f"${self.precio}") 
    
    def venta(self, cantidad):
        """
        Procesa una venta del producto reduciendo el stock si hay unidades suficientes.

        Parámetros:
        - cantidad (int): número de unidades a vender.
        """
        if self.stock > 0:
            if self.stock - cantidad >= 0:
                self.stock -= cantidad
                print(f"Venta realizada! \n{self.nombre}. Nuevo stock: {self.stock}")
            else:
                print(f"{self.nombre}. Stock insuficiente para la venta. Stock actual: {self.stock}. Productos requeridos: {cantidad}")
        else:
            print("No hay stock")
    
    def aplicar_descuento(self, descuento):
        """
        Aplica un descuento al producto siempre que no supere el límite permitido.

        Parámetros:
        - descuento (float): valor decimal del descuento (ejemplo: 0.2 = 20%)
        """
        if descuento > self.__limite_descuento:
            raise ValueError("Descuento mayor al limite")
        self.precio = round(self.precio * (1 - descuento), 2)
    

# ===========================================================
# CLASE HIJA: Electronico

# Representa productos electrónicos. Hereda de Producto e 
# implementa su propia versión de mostrar_info().
# ===========================================================
class Electronico(Producto):
    def mostrar_info(self):
        print(f"--- ELECTRÓNICO --- \n{self.nombre}. \n{self.descripcion}. \nPrecio: ${self.precio} \nStock: {self.stock}")


# ===========================================================
# CLASE HIJA: Ropa

# Representa prendas de vestir con atributos adicionales (talla).
# ===========================================================
class Ropa(Producto):
    
    def __init__(self, nombre, descripcion, precio, stock, talla):
        super().__init__(nombre, descripcion, precio, stock)
        self.talla = talla
        
    def mostrar_info(self):
        print(f"--- ROPA --- \n{self.nombre} \n{self.descripcion} \nPrecio: ${self.precio} \nStock: {self.stock} en talla {self.talla}")


# ===========================================================
# CLASE HIJA DE ELECTRONICO: Videojuegos

# Representa videojuegos con atributos adicionales: plataforma y género.
# ===========================================================

class Videojuegos(Electronico):
    def __init__(self, nombre, descripcion, precio, stock, plataforma, genero):
        """
        Constructor que extiende el de Electrónico con atributos adicionales.

        Parámetros:
        - plataforma (str): consola o sistema (Xbox, PS5, PC, etc.)
        - genero (str): tipo de videojuego (acción, aventura, etc.)
        """
        super().__init__(nombre, descripcion, precio, stock)
        self.plataforma = plataforma  
        self.genero = genero
        
        
    def mostrar_info(self):
        """Muestra la información específica de un videojuego."""
        print(f"--- VIDEOJUEGO --- \n{self.nombre} - {self.genero} \n{self.descripcion}. \nPrecio: ${self.precio} \nCopias disponibles: {self.stock} {self.plataforma}")



tele = Electronico("Televisor", "Televisor 42 pulgadas", 5500, 10)
camisa = Ropa("Camisa", "Camisa de algodón color azul tipo polo", 350, 25, "M")
juego = Videojuegos("Zelda", "Aventura en mundo abierto", 1400, 5, "Xbox", "Aventura")

# Lista polimórfica
Productos = [tele, camisa, juego]

# Cada producto ejecuta su propia versión de mostrar_info()
for p in Productos:
    p.mostrar_info()
    p.aplicar_descuento(0.2)

# Ejemplo de otros métodos
tele.actualizar_stock(20)
camisa.venta(10)
juego.venta(10)