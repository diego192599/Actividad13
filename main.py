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
    def orden_Paquetes(self):
        def quick_sort(lista):
            if len(lista)<=1:
                return lista
            pivote=lista[0]
            mayores=[r for r in lista[1:] if r.paquetes>pivote.paquetes]
            iguales=[r for r in lista[1:] if r.paquetes==pivote.paquetes]
            menor=[r for r in lista[1:] if r.paquetes<pivote.paquetes]
            return quick_sort(mayores)+[pivote]+iguales+quick_sort(menor)
        self.repartidores=quick_sort(self.repartidores)
    def bucar(self,nombre):
        for r in self.repartidores:
            if r.nombre.lower()==nombre.lower():
                return r
        return None
    def ranking(self):
        print("\n Rankin de los repartidores")
        for r in self.repartidores:
            print(r)
    def estadistica(self):
        if not self.repartidores:
            print("No hay datos de repartidores")
            return
        total=0
        for r in self.repartidores:
            total+=r.paquetes
        promedio=total/len(self.repartidores)
        max=self.repartidores[0].paquetes
        min=self.repartidores[0].paquetes
        for r in self.repartidores:
            if r.paquetes>max:
                max=r.paquetes
            if r.paquetes<min:
                min=r.paquetes
        print("\n---Estadistica---")
        print(f"Total de paquetes: {total}")
        print(f"Promedio de paquetes: {promedio:.2f}")

        print("Mayor numeros de entregas: ")
        for r in self.repartidores:
            if r.paquetes==max:
                print(f"{r.nombre} ({r.paquetes})")

        print("Menor numeros de entregas: ")
        for r in self.repartidores:
            if r.paquetes==min:
                print(f"{r.nombre} ({r.paquetes})")
def clasificar_zona(zona):
    match zona.lower():
        case "norte":
            print("Zona norte asignada")
        case "sur":
            print("️ Zona sur asignada")
        case "este":
            print("️ Zona este asignada")
        case "oeste":
            print(" Zona oeste asignada")
        case _:
            print(" Zona no reconocida")
def mostrar_menu():
    print("""
--- MENÚ ---
1. Agregar repartidor
2. Mostrar ranking ordenado por paquetes
3. Buscar repartidor por nombre
4. Ver estadísticas
5. Salir
""")
def main():
    empresa=EmpresaMensjeria

