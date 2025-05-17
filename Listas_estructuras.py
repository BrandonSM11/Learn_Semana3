# Suma de elementos en una lista
numeros = []
while True:
    valor = input("Ingrese un número (o 'fin' para terminar): ")
    if valor.lower() == "fin":
        break
    try:
        numeros.append(int(valor))
    except ValueError:
        print("Valor inválido. Por favor, ingrese un número.")

suma = sum(numeros)
print(f"Suma de los números: {suma}")

# Buscar un elemento en lista
valor_buscar = int(input("Ingrese un valor para buscar en la lista: "))
if valor_buscar in numeros:
    print(f"El valor {valor_buscar} está presente en la lista.")
else:
    print(f"El valor {valor_buscar} no está presente en la lista.")

# Promedio de calificaciones
calificaciones = []
while True:
    calificacion = input("Ingrese una calificación (o 'fin' para terminar): ")
    if calificacion.lower() == "fin":
        break
    try:
        calificaciones.append(float(calificacion))
    except ValueError:
        print("Valor inválido. Por favor, ingrese una calificación.")

promedio = sum(calificaciones) / len(calificaciones)
print(f"Promedio de calificaciones: {promedio}")

# Números pares en una lista
pares = [x for x in numeros if x % 2 == 0]
print(f"Números pares: {pares}")

# Ordenar una lista
numeros_ordenados = sorted(numeros)
print(f"Lista ordenada: {numeros_ordenados}")

# Eliminar duplicados en una lista
numeros_sin_duplicados = list(set(numeros))
print(f"Lista sin duplicados: {numeros_sin_duplicados}")

# Lista al revés
numeros_reversa = numeros[::-1]
print(f"Lista al revés: {numeros_reversa}")

# Contar ocurrencias
valor_contar = int(input("Ingrese un valor para contar ocurrencias: "))
ocurrencias = numeros.count(valor_contar)
print(f"El valor {valor_contar} aparece {ocurrencias} veces en la lista.")

# Encontrar el mayor y menor de una lista
mayor = max(numeros)
menor = min(numeros)
print(f"Mayor valor: {mayor}")
print(f"Menor valor: {menor}")

# Separar pares e impares
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]
print(f"Pares: {pares}")
print(f"Impares: {impares}")