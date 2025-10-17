

import uuid

class Producto:
    """Clase que genra y representa los atributos del producto"""
    def __init__(self, nombre: str, precio: float, stock: int):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def hay_suficiente_stock(self, cantidad: int) -> bool:
        """Comprueba cuanto si hay y cuanto stock hay de los productos"""
        return self.stock >= cantidad

    def actualizar_stock(self, cantidad: int):
        """ con esto actualizamos el stock que hay de un producto despues de un pedido """
        # Se corrigió el error: ahora suma o resta la cantidad, en lugar de reemplazar el stock.
        self.stock += cantidad

    def __str__(self) -> str:
        """ crea una cadena de texto exponiendo las acracteristiucas del producto nombre, precio (2f pa5ra redondear) y el stock"""
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}"



class ProductoElectronico(Producto):
    """ crea un categoria llamada producto elkectronico con herencia de producto"""
    def __init__(self, nombre: str, precio: float, stock: int, garantia: int):
        # Llama al constructor de la clase padre (Producto)
        super().__init__(nombre, precio, stock)
        self.garantia = garantia

    def __str__(self) -> str:
        """ crea una cadena de texto para los productos electronicos con las caracteristicas nombre precio (2f para redondear) stock y a mayores en esta categoria se le añade garantia en años"""
        return (f"Producto Electrónico: {self.nombre} | Precio: ${self.precio:.2f} | "
                f"Stock: {self.stock} | Garantía: {self.garantia} años")



class ProductoRopa(Producto):
    """ se crea una catehgoria de producto productoropa con herencia de producto """
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str):
        # Llama al constructor de la clase padre (Producto)
        super().__init__(nombre, precio, stock)
        self.talla = talla
        self.color = color

    def __str__(self) -> str:
        """crea una cadena de texto con los atributos nombre, precio (2f para redondearlo), stock y a mayores se le añade talla y color"""
        return (f"Producto de Ropa: {self.nombre} | Precio: ${self.precio:.2f} | "
                f"Stock: {self.stock} | Talla: {self.talla} | Color: {self.color}")
    
    """ este codigo crea los productos con sus atributos controla el stock que hay antes y despues del pedido y genra dos subclases productso 
    productoselectronico y producto ropa con atributos garantia , talla y color a mayores que el producto base"""