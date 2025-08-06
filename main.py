class Repartidor:
    def __init__(self,nombre,paquetes,zona):
        if not nombre or not  zona or paquetes<0:
            raise ValueError("Datos no validos")
        self.nombre=nombre
        self.paquetes=paquetes
        self.zona=zona
    def __str__(self):
        return f"{self.nombre} -{self.paquetes} paquetes - Zona:{self.zona}"

class EmpresaMensjeria:
    def __init__(self):
        self.repartidores=[]
    def existeNombre(self,nombre):
        for r in self.repartidores:
            if r.nombre.lower()==nombre.lower():
                return True
        return False
    def agregar(self,repartidor):
        if self.existeNombre(repartidor.nombre):
            print("Este nombre ya esta registrado")
            return
        self.repartidores.append(repartidor)


