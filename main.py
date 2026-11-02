from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


# ------------------------- funciones de apoyo ✅ -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    lista.añadir(Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"))
    lista.añadir(Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"))
    lista.añadir(Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"))
    lista.añadir(Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"))
    lista.añadir(Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"))
    print("  ✓ Datos de prueba cargados")


def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")

    opciones = [
        "1. Añadir",
        "2. Listar",
        "3. Insertar en posición",
        "4. Buscar (lineal)",
        "5. Buscar (binaria)",
        "6. Modificar",
        "7. Eliminar por posición",
        "8. Eliminar por número",
        "9. Ordenar asc",
        "10. Ordenar desc",
        "11. Reversar",
        "12. Copiar",
        "13. Longitud"
    ]

    if extras:
        opciones.append("14. Filtrar por destino")
        opciones.append("15. Mayores de edad")

    opciones.append("C. Cargar datos de prueba")
    opciones.append("0. Volver")

    for opcion in opciones:
        print(opcion)

# ---------------------- MENÚ 1 · MiLista ----------------------

def menu_lista1():
    while True:
        mostrar_opciones("MENÚ 1 · MiLista")
        op = input("Opción: ").strip().upper()

        # 1. AÑADIR
        if op == "1":
            pasajero = leer_pasajero()

            if lista1.añadir(pasajero):
                print("  ✓ Pasajero añadido")
            else:
                print("  ✗ No se pudo añadir")

        # 2. LISTAR
        elif op == "2":
            lista1.listar()

        # 3. INSERTAR EN POSICIÓN
        elif op == "3":
            posicion = leer_entero("Posición a insertar: ")
            pasajero = leer_pasajero()

            antes = lista1.longitud()
            lista1.insertar(posicion, pasajero)

            if lista1.longitud() > antes:
                print("  ✓ Pasajero insertado correctamente")

        # 4. BÚSQUEDA LINEAL
        elif op == "4":
            numero = leer_entero("Número de pasajero a buscar: ")
            posicion = lista1.buscar(numero)

            if posicion != -1:
                print(f"  ✓ Encontrado en posición {posicion}")
                print(" ", lista1.datos[posicion])
            else:
                print("  ✗ Pasajero no encontrado")

        # 5. BÚSQUEDA BINARIA
        elif op == "5":
            numero = leer_entero("Número de pasajero a buscar: ")

            lista1.ordenar_asc()
            print("  Lista ordenada para búsqueda binaria")

            posicion = lista1.buscar_binaria(numero)

            if posicion != -1:
                print(f"  ✓ Encontrado en posición {posicion}")
                print(" ", lista1.datos[posicion])
            else:
                print("  ✗ Pasajero no encontrado")

        # 6. MODIFICAR
        elif op == "6":
            numero = leer_entero("Número de pasajero a modificar: ")
            posicion = lista1.buscar(numero)

            if posicion != -1:
                destino = input("Nuevo destino: ").strip()
                asiento = input("Nuevo asiento: ").strip().upper()

                lista1.modificar(numero, destino, asiento)
                print("  ✓ Pasajero modificado correctamente")
            else:
                print("  ✗ Pasajero no encontrado")

        # 7. ELIMINAR POR POSICIÓN
        elif op == "7":
            posicion = leer_entero("Posición a eliminar: ")
            eliminado = lista1.eliminar_por_posicion(posicion)

            if eliminado is not None:
                print("  ✓ Pasajero eliminado:", eliminado)

        # 8. ELIMINAR POR NÚMERO
        elif op == "8":
            numero = leer_entero("Número de pasajero a eliminar: ")

            antes = lista1.longitud()
            lista1.eliminar_por_valor(numero)

            if lista1.longitud() < antes:
                print("  ✓ Pasajero eliminado correctamente")

        # 9. ORDENAR ASCENDENTE
        elif op == "9":
            lista1.ordenar_asc()
            print("  ✓ Lista ordenada ascendentemente")
            lista1.listar()

        # 10. ORDENAR DESCENDENTE
        elif op == "10":
            lista1.ordenar_desc()
            print("  ✓ Lista ordenada descendentemente")
            lista1.listar()

        # 11. REVERSAR
        elif op == "11":
            lista1.reversar()
            print("  ✓ Lista reversada")
            lista1.listar()

        # 12. COPIAR
        elif op == "12":
            copia = lista1.copiar()
            print("  ✓ Copia de la lista:")
            copia.listar()

        # 13. LONGITUD
        elif op == "13":
            cantidad = lista1.longitud()
            print(f"  ✓ Cantidad de pasajeros: {cantidad}")

        # C. CARGAR DATOS DE PRUEBA
        elif op == "C":
            cargar_datos_prueba(lista1)

        # 0. VOLVER
        elif op == "0":
            break

        else:
            print("  ✗ Opción no válida")



# ---------------------- MENÚ 2 · list de Python ----------------------
def menu_lista2():
    while True:
        mostrar_opciones("MENÚ 2 · List", extras=True)
        op = input("Opción: ").strip().upper()

        #Añadir
        if op=="1":
            pasajero=leer_pasajero()
            if lista2.añadir(pasajero):
                print("  ✓ Pasajero añadido")
            else:
                print("  ✗ No se pudo añadir")
        #Listar
        elif op=="2":
            lista2.listar()

        #Insertar
        elif op=="3":
            posicion = leer_entero("Posición a insertar: ")
            pasajero = leer_pasajero()

            if lista2.insertar(posicion, pasajero):
                print("  ✓ Pasajero insertado correctamente")
            else:
                print("No se pudo insertar")
        #Buscar
        elif op=="4":
            numero=leer_entero("Número de pasajero a buscar: ")
            posicion = lista2.buscar(numero)
            
            if posicion != -1:
                print(f"  ✓ Encontrado en posición {posicion}")
                print(" ", lista2.pasajeros[posicion])
            else:
                print("Pasajero no encontrado")

        # Buscar binario
        elif op == "5":
            numero=leer_entero("Número de pasajero a buscar: ")
            lista2.ordenar_asc()
            print("Ordenado de forma ascendente")
            
            posicion=lista2.buscar_binaria(numero)

            if posicion !=-1:
               print(f"Encontrado en {posicion}")
               print(f" ", lista2.pasajeros[posicion])
            else:
                print("Pasajero no encontrado")
            

        #Modificar
        elif op == "6":
            numero = leer_entero("Número de pasajero a modificar: ")
            posicion = lista2.buscar(numero)

            if posicion != -1:
                destino = input("Nuevo destino: ").strip()
                asiento = input("Nuevo asiento: ").strip().upper()

                lista2.modificar(numero, destino, asiento)
                print("  ✓ Pasajero modificado correctamente")
            else:
                print("  ✗ Pasajero no encontrado")

        # 7. ELIMINAR POR POSICIÓN
        elif op == "7":
            posicion = leer_entero("Posición a eliminar: ")
            eliminado = lista2.eliminar_por_posicion(posicion)

            if eliminado is not None:
                print(" Pasajero eliminado:", eliminado)

        # 8. ELIMINAR POR NÚMERO
        elif op == "8":
            
            numero = leer_entero("Número de pasajero a eliminar: ")
            eliminado= lista2.eliminar_por_valor(numero)

            if eliminado is not None:
                print(" Pasajero eliminado:", eliminado)
            else:
                print("Pasajero no encontrado")

        #Ordenar ascendente
        elif op=="9":
            lista2.ordenar_asc()
            print("Lista ordenada ascendentemente")
            lista2.listar()

        #Ordenar descendente
        elif op=="10":
            lista2.ordenar_desc()
            print("Lista ordenada descendentemente")
            lista2.listar()

        #Reversar
        elif op=="11":
            lista2.reversar()
            print(f"Lista reversada")
            lista2.listar()

        #Copiar
        elif op=="12":
            copia=lista2.copiar()
            print("Lista copiada")
            copia.listar()
        
        #Longitud
        elif op=="13":

            if lista2.tiene_elementos():
            
               print(f"Cantidad de pasajeros: {lista2.longitud()} ")
            else:
               print("La lista está vacía")

        #Filtrar por ciudad
        elif op == "14":
            if lista2.tiene_elementos():
                ciudad = input("Ingresa la ciudad a filtrar: ").strip()

                if ciudad != "":
                    encontrados = lista2.filtrar_por_destino(ciudad)
                    
                    if encontrados:
                        print(f"  Pasajeros que viajan a {ciudad}:")
                        for pasajero in encontrados:
                            print(" ", pasajero)
                    else:
                        print("  No hay pasajeros con ese destino")
                else:
                    print("  Debe ingresar una ciudad")
            else:
                print("  La lista está vacía")

        #Mayores de edad
        elif op=="15":
            if lista2.tiene_elementos():
                mayores=lista2.mayores_de_edad()
                if mayores:
                    print("Pasajeros mayores de edad")
                    for pasajero in mayores:
                        print(pasajero)
                else: 
                    print("No hay mayores de edad")
            else: print("La lista está vacía")

        # C. CARGAR DATOS DE PRUEBA
        elif op == "C":
            cargar_datos_prueba(lista2)
        
                # 0. VOLVER
        elif op == "0":
            break
        
        else:
            print("  ✗ Opción no válida")


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        print("\n===== TAREA LISTAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · MiLista")
        print("2. Menú 2 · list de Python")
        print("0. Salir")

        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "0":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()