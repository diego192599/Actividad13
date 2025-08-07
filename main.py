class Repartidor:
    def __init__(self, nombre, paquetes, zona):
        if not nombre or not zona or paquetes < 0:
            raise ValueError("Datos no válidos")
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona

    def __str__(self):
        return f"{self.nombre} - {self.paquetes} paquetes - Zona: {self.zona}"


class EmpresaMensajeria:
    def __init__(self):
        self.repartidores = []

    def existeNombre(self, nombre):
        for r in self.repartidores:
            if r.nombre.lower() == nombre.lower():
                return True
        return False

    def agregar(self, repartidor):
        if self.existeNombre(repartidor.nombre):
            print("Este nombre ya está registrado")
            return
        self.repartidores.append(repartidor)

    def orden_Paquetes(self):
        def quick_sort(lista):
            if len(lista) <= 1:
                return lista
            pivote = lista[0]
            mayores = [r for r in lista[1:] if r.paquetes > pivote.paquetes]
            iguales = [r for r in lista[1:] if r.paquetes == pivote.paquetes]
            menores = [r for r in lista[1:] if r.paquetes < pivote.paquetes]
            return quick_sort(mayores) + [pivote] + iguales + quick_sort(menores)

        self.repartidores = quick_sort(self.repartidores)

    def buscar(self, nombre):
        for r in self.repartidores:
            if r.nombre.lower() == nombre.lower():
                return r
        return None

    def ranking(self):
        print("\nRanking de los repartidores:")
        for r in self.repartidores:
            print(r)

    def estadistica(self):
        if not self.repartidores:
            print("No hay datos de repartidores")
            return
        total = 0
        for r in self.repartidores:
            total += r.paquetes

        promedio = total / len(self.repartidores)

        max_paquetes = self.repartidores[0].paquetes
        min_paquetes = self.repartidores[0].paquetes

        for r in self.repartidores:
            if r.paquetes > max_paquetes:
                max_paquetes = r.paquetes
            if r.paquetes < min_paquetes:
                min_paquetes = r.paquetes

        print("\n--- Estadísticas ---")
        print(f"Total de paquetes: {total}")
        print(f"Promedio de paquetes: {promedio:.2f}")

        print("Mayor número de entregas:")
        for r in self.repartidores:
            if r.paquetes == max_paquetes:
                print(f"{r.nombre} ({r.paquetes})")

        print("Menor número de entregas:")
        for r in self.repartidores:
            if r.paquetes == min_paquetes:
                print(f"{r.nombre} ({r.paquetes})")


def clasificar_zona(zona):
    match zona.lower():
        case "norte":
            print("Zona norte asignada")
        case "sur":
            print("Zona sur asignada")
        case "este":
            print("Zona este asignada")
        case "oeste":
            print("Zona oeste asignada")
        case _:
            print("Zona no reconocida")


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
    empresa = EmpresaMensajeria()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                try:
                    cantida = int(input("¿Cuantos repartidores se agregaran?: "))
                    for i in range(cantida):
                        print("\n --Ingreso de repartidores--")
                        nombre = input("Nombre: ").strip()
                        paquetes = int(input("Paquetes: "))
                        zona = input("Zona (norte, sur, este, oeste): ").strip()
                        clasificar_zona(zona)
                        repartidor = Repartidor(nombre, paquetes, zona)
                        empresa.agregar(repartidor)
                except ValueError as e:
                    print(f"Error: {e}")
            case "2":
                empresa.orden_Paquetes()
                empresa.ranking()
            case "3":
                nombre = input("Ingrese el nombre del repartidor a buscar: ").strip()
                encontrado = empresa.buscar(nombre)
                if encontrado:
                    print("Repartidor encontrado:")
                    print(encontrado)
                else:
                    print("Repartidor no encontrado")
            case "4":
                empresa.estadistica()
            case "5":
                print("Programa Finalizado")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")


main()
