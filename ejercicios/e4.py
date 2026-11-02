#Ejercicio 4
lista = [1, 3, 2, 3, 4, 3, 5]
v = 3

# Manual
count = 0
for x in lista:
    if x == v:
        count += 1
print(f"{v} aparece {count} veces")

# Propio de python
print(f"{v} aparece {lista.count(v)} veces")



#Ejercicio 5
lista = [1, 2, 3, 4, 5]

# Con bucle
invertida = []
for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])
print(invertida)

# Con slicing (pythonic)
print(lista[::-1])

# Con reversed
print(list(reversed(lista)))



#Ejercicio 6

nums = [1, 3, 2, 3, 4, 1, 5, 2]

# Manual (mantiene orden)
unicos = []
for x in nums:
    if x not in unicos:
        unicos.append(x)
print(unicos)                       # [1, 3, 2, 4, 5]

# Rápido (NO mantiene orden)
print(list(set(nums)))

# Rápido MANTENIENDO orden (Python 3.7+)
print(list(dict.fromkeys(nums)))    # [1, 3, 2, 4, 5]


#Ejercicio 7

nums = [5, 2, 9, 7, 9, 3, 8]

# Dos campeones: mayor y segundo
mayor = float("-inf")
segundo = float("-inf")

for n in nums:
    if n > mayor:
        segundo = mayor         # el que era mayor pasa a segundo
        mayor = n
    elif n > segundo and n < mayor:
        segundo = n

print(f"Mayor: {mayor}")
print(f"Segundo: {segundo}")



#Ejercicio 8

a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]

resultado = []
i = j = 0

# Recorremos las dos listas a la par
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        resultado.append(a[i])
        i += 1
    else:
        resultado.append(b[j])
        j += 1

# Añadimos lo que quede de la más larga
resultado.extend(a[i:])
resultado.extend(b[j:])

print(resultado)                    # [1, 2, 3, 4, 5, 6, 7, 8, 10]