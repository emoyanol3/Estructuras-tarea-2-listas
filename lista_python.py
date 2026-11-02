from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Las mismas operaciones usando los métodos del list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):                      # ✅ resuelto
        self.pasajeros.append(pasajero)
        return True

    def listar(self):                                 # ✅ resuelto
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    # ---------------- ✍ IMPLEMENTA (tabla 3.2 de la guía) ----------------
    def insertar(self, posicion, pasajero):

        if posicion < 0 or posicion > len(self.pasajeros):
           print("Posición no válida")
           return False

        self.pasajeros.insert(posicion, pasajero)
        return True
        

    def buscar(self, numero):

        for i, pasajero in enumerate(self.pasajeros):
            if pasajero.numero == numero:
                        return i
        return -1

    def buscar_binaria(self, numero):

        pos = bisect_left(self.pasajeros, numero, key=lambda p: p.numero)

        if pos < len(self.pasajeros) and self.pasajeros[pos].numero == numero:
            return pos

        return -1 

    def modificar(self, numero, nuevo_destino, nuevo_asiento):

        pos = self.buscar(numero)
        if pos == -1:
            print(numero, "no existe")
            return
        self.pasajeros[pos].destino = nuevo_destino
        self.pasajeros[pos].asiento = nuevo_asiento

    def eliminar_por_posicion(self, posicion):

        if posicion < 0 or posicion >= len(self.pasajeros):
            print("Posición no válida")
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, numero):
        pos=self.buscar(numero)
        if pos==-1:
            print("No existe")
            return
        return self.eliminar_por_posicion(pos)


    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
            nueva = ListaPython()
            nueva.pasajeros = self.pasajeros.copy()
            return nueva

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):           # solo Lista 2
            encontrados = []

            for pasajero in self.pasajeros:
                if pasajero.destino.lower() == destino.lower():
                    encontrados.append(pasajero)

            return encontrados

    def mayores_de_edad(self):                        # solo Lista 2
            mayores = []

            for pasajero in self.pasajeros:
                if pasajero.es_mayor_de_edad():
                    mayores.append(pasajero)

            return mayores

    def tiene_elementos(self):
         if self.longitud()!=0:
              return True
         return False
         