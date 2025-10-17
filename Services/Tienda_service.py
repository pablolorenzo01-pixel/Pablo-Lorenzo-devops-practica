
import uuid
""" uuid nos genara un identificador unico"""
from typing import List
from Models.Usuario import Usuario
from Models.Producto import Producto
from Models.Pedido import Pedido

class TiendaService:
    """ crea una clase para los servicios de la tienda con listas de usuarios productos y pedidos"""
    def __init__(self):
        self.usuarios: List[Usuario] = []
        self.productos: List[Producto] = []
        self.pedidos: List[Pedido] = []

    def registrar_usuario(self, nuevo_usuario: Usuario):
        """se encarga de regsitrar nuevos usuariso entrantes en la tienda"""
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario registrado: {nuevo_usuario.nombre}")
        return nuevo_usuario

    def anadir_producto(self, producto: Producto):
        """ actua parecido al codigo anterior pero esta vez añadeindo prodctos al stock"""
        self.productos.append(producto)

    def listar_productos(self):
        """ crea una lista con todos los productos disponibles en stock"""
        print("\n--- Inventario de Productos ---")
        for producto in self.productos:
            print(producto)

    def realizar_pedido(self, cliente: Usuario, productos_con_cantidad: List[dict]):
        """ crea el proceso de un pedido, con función de controlar el stock y si no disponen de stock devueleve un error y si se encuentra stock te devuelve que el pedido se hizo correctamente"""
        for item in productos_con_cantidad:
            producto = item['producto']
            cantidad = item['cantidad']
            if not producto.hay_suficiente_stock(cantidad):
                print(f"Error: No hay suficiente stock para {producto.nombre}.")
                return None
        
        for item in productos_con_cantidad:
            producto = item['producto']
            cantidad = item['cantidad']
            producto.actualizar_stock(-cantidad)
            
        nuevo_pedido = Pedido(cliente, productos_con_cantidad)
        self.pedidos.append(nuevo_pedido)
        print(f"\nPedido realizado con éxito por {cliente.nombre}!")
        return nuevo_pedido

    def historico_pedidos_usuario(self, usuario_id: uuid.UUID):
        """crea una lista con los pedidos de un usuario en especifico"""
        pedidos_usuario = [p for p in self.pedidos if p.cliente.id == usuario_id]
        # Ordenar por fecha (más reciente primero)
        pedidos_usuario.sort(key=lambda x: x.fecha, reverse=True)
        return pedidos_usuario
    """ este codigo genara la estructura de la tienda con listas de los pedidos usuarios y productos y creando los pedidos identificando el stock disponible y viendo si el pedido puede realizarse"""