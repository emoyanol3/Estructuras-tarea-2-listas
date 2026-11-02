from pasajero import Pasajero


class MiLista:
    """Lista construida a mano sobre un arreglo de tamaño fijo.
    datos     -> [p1, p2, p3, None, None, ...]
    capacidad -> total de cajones     cantidad -> cajones ocupados
    ⛔ Sin append, insert, pop, remove, sort, reverse, copy, len, in, slicing.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):                      # ✅ resuelto
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        self.datos[self.cantidad] = pasajero          # primer cajón libre
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ resuelto
        if self.cantidad == 0:
            print("  (lista vacía)")
            return
        for i in range(self.cantidad):
            print(f"  [{i}] {self.datos[i]}")

    # ---------------- ✍ IMPLEMENTA (tabla 3.1 de la guía) ----------------
    def insertar(self, posicion, pasajero):

        if self.cantidad == self.capacidad:
            print("La lista está llena")
            return
        if posicion < 0 or posicion > self.cantidad:
            print("Posición no válida")
            return
        i = self.cantidad                   # empiezo por el final
        while i > posicion:
            self.datos[i] = self.datos[i - 1]   # muevo cada uno un lugar a la derecha
            i = i - 1
        self.datos[posicion] = pasajero        # el nuevo entra en el hueco
        self.cantidad = self.cantidad + 1
        return True

    def buscar(self, numero):

        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def buscar_binaria(self, numero):

        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio].numero == numero:
                return medio                # lo encontré
            elif self.datos[medio].numero < numero:
                izq = medio + 1             # está a la derecha
            else:
                der = medio - 1             # está a la izquierda
        return -1                           # no está


    def modificar(self, numero, nuevo_destino, nuevo_asiento):

        pos = self.buscar(numero)
        if pos == -1:
            print(numero, "no existe")
            return
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento

    def eliminar_por_posicion(self, posicion):

        if posicion < 0 or posicion >= self.cantidad:
            print("Posición no válida")
            return None
        valor = self.datos[posicion]        # guardo el que voy a quitar

        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]   # muevo cada uno un lugar a la izquierda
        self.datos[self.cantidad - 1] = None    # el último cajón queda vacío
        self.cantidad = self.cantidad - 1
        return valor

    def eliminar_por_valor(self, numero):
        
        pos = self.buscar(numero)
        if pos == -1:
            print(numero, "no existe")
            return None
        return self.eliminar_por_posicion(pos)

    def ordenar_asc(self):

        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].numero > self.datos[i + 1].numero:
                    aux = self.datos[i]                 # intercambio con
                    self.datos[i] = self.datos[i + 1]   # una variable
                    self.datos[i + 1] = aux             # auxiliar

    def ordenar_desc(self):

        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].numero < self.datos[i + 1].numero:
                    aux = self.datos[i]                 # intercambio con
                    self.datos[i] = self.datos[i + 1]   # una variable
                    self.datos[i + 1] = aux             # auxiliar

    def reversar(self):

        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq = izq + 1
            der = der - 1

    def copiar(self):

        nueva = MiLista(self.capacidad)
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad