# Contar del 1 al 10
print("Contar del 1 al 10:")
for i in range(1, 11):
    print(i)

# Contador descendente
print("\nContador descendente:")
i = 10
while i >= 1:
    print(i)
    i -= 1

# Sumar N números
n = 10
suma = 0
print(f"\nSuma de los primeros {n} números naturales:")
for i in range(1, n + 1):
    suma += i
print(f"La suma es: {suma}")

# Tabla de multiplicar
numero = 5
print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Suma hasta número ingresado
numero = int(input("\nIngrese un número: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print(f"La suma de los números desde 1 hasta {numero} es: {suma}")

# Número secreto
numero_secreto = 50
intentos = 0
print("\nJuego de adivinar el número secreto:")
while True:
    intento = int(input("Ingrese su intento: "))
    intentos += 1
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        print(f"Felicidades! Has adivinado el número secreto en {intentos} intentos.")
        break

# Cuenta regresiva
numero = 10
print("\nCuenta regresiva:")
for i in range(numero, 0, -1):
    print(i)

# Múltiplos de 3 entre 1 y 100
print("\nMúltiplos de 3 entre 1 y 100:")
for i in range(1, 101):
    if i % 3 == 0:
        print(i)

# Factorial de un número
numero = 5
factorial = 1
print(f"\nFactorial de {numero}:")
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es: {factorial}")

# Dibujar una pirámide de asteriscos
altura = 5
print("\nPirámide de asteriscos:")
for i in range(altura):
    for j in range(altura - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()