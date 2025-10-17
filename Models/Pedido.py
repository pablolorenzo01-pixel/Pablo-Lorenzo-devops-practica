import uuid 
import datetime
from typing import List, Dict
""" uuid nos genara un identificador unico"""
""" datetime nos asigna un fecha utomatica """
""" ayuda a entender que la variable productos_con_cantidad debe ser una List """
from Models.Usuario import Usuario
from Models.Producto import Producto
""" aqui invocamos Usuario y producto desde otra carpeta"""

class Pedido:
    def __init__(self, cliente: Usuario, productos_con_cantidad: List[Dict]):
        self.id = uuid.uuid4()
        self.fecha = datetime.datetime.now()
        self.cliente = cliente
        self.productos_con_cantidad = productos_con_cantidad
        """ Con esto al pedido le asiganmos los atributos ID fecha cliente y cantidad """


    def __str__(self) -> str:
        
        """Su función es indicar que debe representarse el objeto como una cadena de texto """
   
        pedido_str = (
            f"Pedido ID: {self.id}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Productos:\n"
    )
        """ Aqui asignamos una linea de textos que espondra los datos generados """
   
        for item in self.productos_con_cantidad:
            pedido_str += f"    - {item['producto'].nombre} (x{item['cantidad']})\n"

    # 3. Retornar la cadena completa
        return pedido_str
""" con esto nos retorna el texto final que muestra el pedido"""
    
""" Con este codigo registramos los pedidos asignadoles un ID y fecha y asigna el cliente el cual lo ha encargado
        y la cantidad de dicho producto """