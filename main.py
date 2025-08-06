class Repartidor:
    def __init__(self,nombre,paquetes,zona):
        if not nombre or not  zona or paquetes<0:
            raise ValueError("Datos no validos")
        self.nombre=nombre
        self.paquetes=paquetes
        self.zona=zona
