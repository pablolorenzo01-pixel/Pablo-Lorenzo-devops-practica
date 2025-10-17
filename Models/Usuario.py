import uuid
""" genara un identificador unico que nos ayudara para generara el id"""
class Usuario:
    """crea la clase usurio con atributos id, nombre y email"""
    def __init__(self, nombre: str, email: str):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.email = email
    """identifica al usuario como usuario y no como admin"""
    def es_admin():
        return False

    def __str__(self) -> str:
        """crea uan cadena de texto para usuario con nombre, si es admin y su email"""
        return f"Usuario: {self.nombre} admin:({Usuario.es_admin()}) | Email: {self.email}"
    
class Cliente(Usuario):
    def __init__(self, nombre, email, codigo_postal):
        super().__init__(nombre,email)
        self.codigo_postal = codigo_postal 
        """ crea la subclase cliente de usuario con un atributo a mayores apartes de los de la clse padre que es codigo postal"""
class Admin(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
    def es_admin():
        return True
    """ crea subclase admin apartir de la clase padre usuario y lo identifica como admin para diferenciarlo de usuario"""

    """ este codigo crea la clase usuario para atrubuirlo a la demanda de un pedido y creamos dos subclase usuario y admin para diferenciar roles """