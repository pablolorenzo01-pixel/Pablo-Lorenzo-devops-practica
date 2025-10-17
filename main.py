# Se asume que la estructura de carpetas es Tienda_online/models y Tienda_online/services
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from Services.Tienda_service import TiendaService
from Models.Producto import Producto, ProductoElectronico, ProductoRopa
from Models.Usuario import Usuario, Cliente, Admin

""" genara los usuariso que interectuaran con la tienda y inicia el proceso"""
def main():
    print("--- Inicializando la tienda ---")
    tienda = TiendaService()

  
    cliente1 = Cliente("Ana García", "ana.g@email.com", 36201)
    cliente2 = Cliente("Luis Pérez", "luis.p@email.com", 36329)        
    cliente3 = Cliente("Marta Gómez", "marta.g@email.com", 36208)
    Administrador = Admin("Carlos Ruiz", "carlos.r@email.com")

    tienda.registrar_usuario(cliente1)
    tienda.registrar_usuario(cliente2)
    tienda.registrar_usuario(cliente3)
    tienda.registrar_usuario(Administrador)
    

    """crea los productos los precios las cantidades y los atrubutos añadidos como la garantia y genara una lista con ellos"""
    print("\n--- Añadiendo productos al inventario ---")
    prod1 = ProductoElectronico("Laptop Gamer", 1200.0, 10,12)
    prod2 = ProductoElectronico("Teclado Mecánico", 85.50, 25,12)
    prod3 = ProductoRopa("Sudadera", 45.0, 15,"M", "Naranja")
    prod4 = ProductoRopa("Pantalon", 30.0, 50,"L","Blanco")
    prod5 = Producto("Vajilla", 60.0, 20)

    tienda.anadir_producto(prod1)
    tienda.anadir_producto(prod2)
    tienda.anadir_producto(prod3)
    tienda.anadir_producto(prod4)
    tienda.anadir_producto(prod5)

   
    tienda.listar_productos()

    """genara los pedidos"""
    print("\n--- pedidos ---")

    """primer pedidos """
    pedido1 = tienda.realizar_pedido(cliente1, [
        {'producto': prod1, 'cantidad': 1},
        {'producto': prod2, 'cantidad': 2}
    ])
    if pedido1:
        print(f"Detalles del {pedido1}")
    
    """segudno pedido"""
    pedido2 = tienda.realizar_pedido(cliente2, [
        {'producto': prod3, 'cantidad': 1},
        {'producto': prod4, 'cantidad': 10}
    ])
    if pedido2:
        print(f"Detalles del {pedido2}")

    """ tercer pedido """
    pedido3 = tienda.realizar_pedido(cliente3, [
        {'producto': prod5, 'cantidad': 5},
        {'producto': prod1, 'cantidad': 1}
    ])
    if pedido3:
        print(f"Detalles del {pedido3}")

    """comprueba el historial de pedidos del cliente"""
    print("\n--- Historial de pedidos de Luis Pérez ---")
    pedidos_luis = tienda.historico_pedidos_usuario(cliente2.id)
    if pedidos_luis:
        for pedido in pedidos_luis:
            print(pedido)
    else:
        print("No se encontraron pedidos para este usuario.")

    """Genara el stock despues de los pedidos actualizandolo """
    tienda.listar_productos()

if __name__ == "__main__":
    main()

    """ con este codigo controlamos todas las funciones de la tienda generando e indicando los suauraios y los pedidos genrando los pedidos con acada producto y usuario actuaqlizando el stock y el historial de pedidos del cliente"""